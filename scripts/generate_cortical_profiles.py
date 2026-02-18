import os
import re
import csv
import json
from collections import defaultdict
import gzip

import numpy as np

from pathlib import Path

import uvloop

import databases
import pandas as pd

from lib.db import silo_db, crop_db, marmoset_db

class Region:
    def __init__(self, record):
        self.id = record.id
        self.name = record.name
        self.code = record.code
        self.parent_id = record.parent_id
        self.color_code = record.color_code
        self._3dbar_index = record._3dbar_index
        self.children = []
        self.is_leaf = True

    def __repr__(self):
        return f'Region {self.code} [{len(self.children)}]'

def traverse(regions, nodes):
    for n in nodes:
        if n.is_leaf:
            name = n.name[0].lower() + n.name[1:]
        else:
            name = n.name
        if n.color_code == '#00FFAB':
            _node = {
                'name': name + ' (Structural)',
                'rgb': n.color_code,
            }
        else:
            _node = {
                'name': name,
                'rgb': n.color_code
            }
        if len(n.children) > 0:
            _node['children'] = []
        else:
            """
                'openminds/ParcellationEntityVersion': [
                    '19285775-222e-4ccf-86ae-04f4c4779966',
                    '39a61f7b-b39a-442d-b57a-910686ad7e1c'
                ]
            """
            _node['ebrains'] = {
            }
        regions.append(_node)
        if len(n.children) > 0:
            traverse(_node['children'], n.children)

async def main():
    try:
        os.makedirs('output/feature')
    except FileExistsError:
        # feature folder to be pushed to siibra-configurations
        pass
    try:
        os.makedirs('output/calbindin_bucket')
    except FileExistsError:
        # bucket folder to be loaded to ebrains dataset storage
        pass
    await marmoset_db.connect()
    layer_breakpoint = defaultdict(dict)
    meta_value = {
        'layer_breakpoint': layer_breakpoint
    }
    meta = {
        'version': '1.0',
        'value': meta_value
    }
    lookup = {}
    query = 'SELECT id, name, code, parent_id, color_code, _3dbar_index FROM region'
    regions = []
    _regions = await marmoset_db.fetch_all(query)
    root = None
    for r in _regions:
        lookup[r.id] = Region(r)
        if r.id == 2643:
            lookup[r.id].is_leaf = False
        if r.parent_id is None:
            root = lookup[r.id]
    for _id in lookup.keys():
        #, 'parent', lookup[r.parent_id])
        r = lookup[_id]
        if r.parent_id is None:
            continue
        parent = lookup[r.parent_id]
        parent.is_leaf = False
        parent.children.append(r)

    traverse(regions, [root])
    await marmoset_db.disconnect()


    indices = {}
    patt = r'\(.*?\)'
    fname_re = re.compile(r'(?P<case_id>CJ\d+[a-z]*)_profile_(?P<area>.*?)\.npy', re.I)
    centroid = pd.read_csv('centroids.csv')
    breakpoints = pd.read_excel('relative_cortical_depth_layers_1to3_and_5to6.xlsx')
    cent = {}
    for index, row in centroid.iterrows():
        cent[row.area_id] = [
            row.coord_x,
            row.coord_y,
            row.coord_z
        ]
    for idx, r in enumerate(sorted(lookup.values(), key=lambda v: v._3dbar_index)):
        if r._3dbar_index == 99:
            continue
        if r.is_leaf:
            name = r.name[0].lower() + r.name[1:]
            indices[name] = [{
                'label': r._3dbar_index,
                'volume': 0
            }]
        else:
            name = r.name
        code = r.code.replace('/', '-')
        code = re.sub(patt, '', code).strip()
        if not os.path.exists(f'../data/calbindin_profiles/CJ200L_profile_{code}.npy.gz'):
            print (ValueError('!missing CJ200L npy for ' + code))
            continue
        if not os.path.exists(f'../data/calbindin_profiles/CJ205_profile_{code}.npy.gz'):
            print (ValueError('!missing CJ205L npy for ' + code))
            continue
        if not os.path.exists(f'../data/calbindin_profiles/CJ1741_profile_{code}.npy.gz'):
            print (ValueError('!missing CJ1741 npy for ' + code))
            continue
        with open(f'output/calbindin_bucket/{code}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['case_id', 'depth', 'density_5', 'density_25', 'density_50', 'density_75', 'density_95'])
            for p in Path('../data/calbindin_profiles').glob(f'*_profile_{code}.npy.gz'):
                with gzip.open(p, 'rb') as f:
                    arr = np.load(f)
                matches = fname_re.match(p.name)
                if matches is not None:
                    case_id = matches.group('case_id')
                    for i in range(100):
                        depth = (i + 1) * 0.01
                        density = [
                            arr[0, i],
                            arr[1, i],
                            arr[2, i],
                            arr[3, i],
                            arr[4, i]
                        ]
                        writer.writerow([case_id, depth, *density])
                bp = breakpoints[(breakpoints.case_id == case_id) & (breakpoints.human_abbrev == code)]
                d13 = layer_breakpoint[code].setdefault('depth_1_3', {})
                d56 = layer_breakpoint[code].setdefault('depth_5_6', {})
                d13[case_id] = float(bp.depth_1_3.iloc[0])
                d56[case_id] = float(bp.depth_5_6.iloc[0])

        area = matches.group('area')
        coordinate = cent[r._3dbar_index]
        # generate needed feature files for siibra-configurations to pick up and supply to the UI for query
        with open(f'output/feature/calbindin-profile-{code}.json', 'w') as f:
            feature = {
                "@id": f"marmoset-nencki-monash-template--calbindin-profile-{code}",
                "@type": "siibra/feature/profile/marmosetcelldensity/v0.1",
                "region": r.name,
                "unit": "detected cells / 0.1mm3",
                "location": {
                    "@type": "siibra/location/point/v0.1",
                    "space": {
                        "@id": "nencki/nm/referencespace/v1.0.0/MARMOSET_NM_NISSL_2020"
                    },
                    "coordinate": coordinate
                },
                "ebrains": {
                    "openminds/Species": "627bac2f-2b4c-4f2d-ae4e-9373a7f430f2",
                    #"openminds/Dataset": "69121624-98ee-4150-a09e-5e4661836513",
                    #"openminds/DatasetVersion": ""
                },
                #"file": f"https://data-proxy.ebrains.eu/api/v1/buckets/marmoset-nencki-monash-template/features/calbindin/{code}.csv",
                "file": f"{code}.csv",
                "repository": {
                    "@type": "siibra/repository/zippedfile/v1.0.0",
                    "url": "https://data-proxy.ebrains.eu/api/v1/buckets/marmoset-nencki-monash-template/features/calbindin_profile.zip"
                },
				"decoder": {
					"@type": "siibra/decoder/csv",
					"delimiter": ",",
					"header": 'infer',
					"skiprows": None,
					"engine": "python",
					"index_col": False
				},

            }
            json.dump(feature, f, indent=4)
        with open('output/calbindin_bucket/meta.json', 'w') as f:
            json.dump(meta, f, indent=4)


if __name__ == '__main__':
    uvloop.run(main())

