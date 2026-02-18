import os
import re
import csv
import json
from collections import defaultdict

import numpy as np

from pathlib import Path

import uvloop

import databases
import pandas as pd

from lib.db import silo_db, crop_db, marmoset_db
import requests


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
    await marmoset_db.connect()
    regions = []
    """
    layer_breakpoint = defaultdict(dict)
    meta_value = {
        'layer_breakpoint': layer_breakpoint
    }
    meta = {
        'version': '1.0',
        'value': meta_value
    }
    """
    lookup = {}
    query = 'SELECT id, name, code, parent_id, color_code, _3dbar_index FROM region'
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


    #indices = {}
    patt = r'\(.*?\)'
    fname_re = re.compile(r'(?P<case_id>CJ\d+[a-z]*)_profile_(?P<area>.*?)\.npy', re.I)
    """
    centroid = pd.read_csv('centroids.csv')
    cent = {}
    for index, row in centroid.iterrows():
        cent[row.area_id] = [
            row.coord_x,
            row.coord_y,
            row.coord_z
        ]
    """
    for idx, r in enumerate(sorted(lookup.values(), key=lambda v: v._3dbar_index)):
        if r._3dbar_index == 99:
            continue
        if r.is_leaf:
            name = r.name[0].lower() + r.name[1:]
            """
            indices[name] = [{
                'label': r._3dbar_index,
                'volume': 0
            }]
            """
        else:
            name = r.name
        code = r.code.replace('/', '-')
        code = re.sub(patt, '', code).strip()
        url = f'https://proxy.mrosa.org/v3_0/feature/marmoset-nencki-monash-template--calbindin-profile-{code}/plotly?template=plotly_white'
        res = requests.get(url)
        ok = False
        if not os.path.exists(f'../data/calbindin_profiles/CJ200L_profile_{code}.npy.gz'):
            ok = True
        if res.status_code == 404:
            print (code, res.status_code, '=>', 'ok' if ok else 'missing !!!')
        else:
            print (code, res.status_code)


if __name__ == '__main__':
    uvloop.run(main())

