import os
import re
import json
import uvloop
import databases
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
            print (n, 'is leaf')
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

    """
        space ebrain data
            "openminds/DatasetVersion": "d69b70e2-3002-4eaf-9c61-9c56f019bbc8",
            "openminds/Dataset": "5a16d948-8d1c-400c-b797-8a7ad29944b2",
            "openminds/BrainAtlasVersion": [
                "2db81b5c-6192-498b-b4c2-7e4906929527",
                "94340f2a-7e00-4e7a-9389-ce9f5e8824c2",
                "636555e4-8a95-4be2-ac25-dd53b71caa08",
                "ed538f38-5d2e-4efb-b401-1e524468c96c"
            ]
    """
    space = {
        "@id": "nencki/nm/parcellationatlas/v1.0.0/MARMOSET_NM",
        "@type": "siibra/parcellation/v0.0.1",
        "name": "Marmoset Nencki-Monash Atlas (2020)",
        "shortName": "marmoset_nm_2020",
        "modality": "cytoarchitecture",
        "@version": {
            "name": "1.0.0"
        },
        "species": "Callithrix Jacchus",
        "regions": regions,
        "ebrains": {
            "minds/core/species/v1.0.0": "0ea4e6ba-2681-4f7d-9fa9-49b915caaac9",
            "openminds/Species": "627bac2f-2b4c-4f2d-ae4e-9373a7f430f2",
        },
        "publications": [
            {
                'name': 'Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas',
                #'description': 'This dataset contains the Nencki–Monash template. The template represents a morphological average of 20 brains of young adult individuals obtained by 3D reconstructions generated from Nissl-stained serial sections. The template was generated taking into account morphological features of the individual brains and the borders of clearly defined cytoarchitectural areas. This allows direct estimates of the most likely coordinates of each cortical area, as well as quantification of the margins of error involved in assigning voxels to areas, and preserves quantitative information about the laminar structure of the cortex. The template also provides spatial transformations between other commonly used marmoset brain templates, thus enabling integration with magnetic resonance imaging (MRI) and tracer-based connectivity data.',
                'description': 'This atlas consists of probabilistic localizations of 116 cytoarchitectural areas of the marmoset cerebral cortex, along with the related parcellation of the most likely area at a given location. This probabilistic parcellation was based on Nissl-based cytoarchitecture in twenty individuals who contributed to the template. The taxonomy, nomenclature, and cytoarchitectural criteria were derived from the Paxinos et al. (2012) atlas.',
                'citation': 'Piotr Majka, Sylwia Bednarek, Jonathan M. Chan, Natalia Jermakow, Cirong Liu, Gabriela Saworska, Katrina H. Worthy, Afonso C. Silva, Daniel K. Wójcik, Marcello G.P. Rosa, Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas, NeuroImage, Volume 226, 2021, 117625, ISSN 1053-8119, https://doi.org/10.1016/j.neuroimage.2020.117625. (https://www.sciencedirect.com/science/article/pii/S1053811920311101)',
                'url': 'https://doi.org/10.1016/j.neuroimage.2020.117625',
				'authors': [
					'Piotr Majka',
					'Sylwia Bednarek',
					'Jonathan M. Chan',
					'Natalia Jermakow',
					'Cirong Liu',
					'Gabriela Saworska',
					'Katrina H. Worthy',
					'Afonso C. Silva',
					'Daniel K. Wójcik',
					'Marcello G.P. Rosa'
				],

                'license': 'Creative Commons Attribution 4.0 (CC-BY)'
            }
        ]

    }
    with open('../siibra-configurations/parcellations/marmoset_nm.json', 'w') as f:
        f.write(json.dumps(space, indent='\t', ensure_ascii=False) + '\n')

    indices = {}
    for r in sorted(lookup.values(), key=lambda v: v._3dbar_index):
        if r.is_leaf:
            name = r.name[0].lower() + r.name[1:]
            indices[name] = [{
                'label': r._3dbar_index,
                'volume': 0
            }]
        else:
            name = r.name

    """
        "sparsemap": {
            "is_sparsemap": True,
            "cached": False,
            "url": ""
        },
    """
    map_ = {
        '@id': 'siibra-map-v0.0.1_marmoset-nm-labelled',
        "@type": "siibra/map/v0.0.1",
        "space": {
            "@id": "nencki/nm/referencespace/v1.0.0/MARMOSET_NM_NISSL_2020"
        },
        "parcellation": {
            "@id": "nencki/nm/parcellationatlas/v1.0.0/MARMOSET_NM"
        },
        "volumes": [
            {
                "@type": "siibra/volume/v0.0.1",
                "providers": {
                    "neuroglancer/precomputed": "https://data-proxy.ebrains.eu/api/v1/buckets/marmoset-nencki-monash-template/segmentations",
                    "neuroglancer/precompmesh": "https://data-proxy.ebrains.eu/api/v1/buckets/marmoset-nencki-monash-template/segmentations",
                }
            }
        ],
        "indices": indices
    }
    cont_volumns = []
    indices = {}
    patt = r'\(.*?\)'
    for idx, r in enumerate(sorted(lookup.values(), key=lambda v: v._3dbar_index)):
        vol_idx = len(cont_volumns)
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
        fn = f'probability_map_{r._3dbar_index:03d}_{code}.nii.gz'
        if not os.path.exists('/home/baishi/tmp/tmp/probability_map/' + fn):
            raise ValueError(fn)
        cont_volumns.append({
            '@type': 'siibra/volume/v0.0.1',
            'providers': {
                'nii': f'https://data-proxy.ebrains.eu/api/v1/public/buckets/marmoset-nencki-monash-template/probability_map/{fn}'
            }
        })
        indices[name] = [
            {'volume': vol_idx}
        ]
    map_continuous = {
        '@id': 'siibra-map-v0.0.1_marmoset-nm-continuous',
        'name': 'Marmoset Nencki-Monash Atlas',
        "@type": "siibra/map/v0.0.1",
        "space": {
            "@id": "nencki/nm/referencespace/v1.0.0/MARMOSET_NM_NISSL_2020"
        },
        "parcellation": {
            "@id": "nencki/nm/parcellationatlas/v1.0.0/MARMOSET_NM"
        },
        "sparsemap": {
            'is_sparsemap': True,
            'cached': False,
            'url': ''
        },
        "volumes": cont_volumns,
        "indices": indices
    }

    with open('../siibra-configurations/maps/marmoset_nm-cortical-labelled.json', 'w') as f:
        f.write(json.dumps(map_, indent='\t', ensure_ascii=False) + '\n')

    with open('../siibra-configurations/maps/marmoset_nm-cortical-continuous.json', 'w') as f:
        f.write(json.dumps(map_continuous, indent='\t', ensure_ascii=False) + '\n')

if __name__ == '__main__':
    uvloop.run(main())
