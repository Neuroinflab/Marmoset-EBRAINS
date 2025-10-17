import os
import re
import json
import csv

import asyncio

from databases import Database

import openminds.latest as om

def to_camel_case(text):
    text = text[0].lower() + text[1:]
    return re.sub(r"[_]([a-zA-Z])", lambda x: x[1].upper(), text)

async def gen_atlas(terms, term_versions):
    meta = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@id': 'https://openminds.om-i.org/instances/brainAtlas/MarmosetNMA',
        '@type': 'https://openminds.om-i.org/types/BrainAtlas',
        'abbreviation': 'MarmosetNMA',
        'author': None,
        'custodian': None,
        'description': 'The Marmoset Nencki-Monash Atlas is a three dimensional (3D) probabilistic  brain atlas reconstructed from 20 young adult marmoset monkeys (Callithrix jacchus) and segmented based on the cytoarchitectonic analysis of the serial Nissl-stained sections of those brains.',
        'digitalIdentifier': {
            '@id': 'https://search.kg.ebrains.eu/instances/6eb874e1-63b3-4889-948a-0d3987cb249b'
        },
        'fullName': 'Marmoset Nencki-Monash Probabilistic Cytoarchitectonic Brain Atlas',
        'hasTerminology': {
            '@type': 'https://openminds.om-i.org/types/ParcellationTerminology',
            'dataLocation': None,
            'hasEntity': [{'@id': t} for t in terms],
            'ontologyIdentifier': None,
        },
        'hasVersion': [{
            '@id': 'https://openminds.om-i.org/instances/brainAtlasVersion/MarmosetNMA_v1'
        }],
        'homepage': 'https://www.marmosetbrain.org',
        'howToCite': 'Piotr Majka, Sylwia Bednarek, Jonathan M. Chan, Natalia Jermakow, Cirong Liu, Gabriela Saworska, Katrina H. Worthy, Afonso C. Silva, Daniel K. Wójcik, Marcello G.P. Rosa, Histology‐Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas, NeuroImage, Volume 226, 2021, 117625, ISSN 1053-8119, https://doi.org/10.1016/j.neuroimage.2020.117625. (https://www.sciencedirect.com/science/article/pii/S1053811920311101)',
        'shortName': 'Marmoset Nencki-Monash Atlas',
        'usedSpecies': {
            '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus'
        }
    }
    meta_version = meta.copy()
    del meta_version['hasVersion']
    del meta_version['usedSpecies']
    meta_version['@id'] = 'https://openminds.om-i.org/instances/brainAtlasVersion/MarmosetNMA_v1'
    meta_version['@type'] = 'https://openminds.om-i.org/types/BrainAtlasVersion'
    meta_version['accessibility'] = {
        '@id': 'https://openminds.om-i.org/instances/productAccessibility/freeAccess'
    }
    meta_version['coordinateSpace'] = {
        '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMA_v1'
    }
    meta_version['copyright'] = None
    meta_version['fullDocumentation'] = None
    meta_version['fullName'] = None
    meta_version['funding'] = None
    meta_version['hasTerminology'] = {
        '@type': 'https://openminds.om-i.org/types/ParcellationTerminologyVersion',
        'dataLocation': None,
        'hasEntity': [{'@id': t} for t in term_versions],
        'ontologyIdentifier': None
    }

    meta_version['isAlternativeVersionOf'] = None
    meta_version['isNewVersionOf'] = None
    meta_version['keyword'] = None
    meta_version['license'] = {
        '@id': 'https://openminds.om-i.org/instances/licenses/ccBy4.0'
    }
    meta_version['majorVersionIdentifier'] = None
    meta_version['ontologyIdentifier'] = None
    meta_version['otherContribution'] = None
    meta_version['relatedPublication'] = [{
        '@id': 'https://doi.org/10.1016/j.neuroimage.2020.117625'
    }]
    meta_version['releaseDate'] = None
    meta_version['repository'] = None
    meta_version['supportChannel'] = [
        'support@marmosetbrain.org'
    ]
    meta_version['type'] = {
        '@id': 'https://openminds.om-i.org/instances/atlasType/probabilisticAtlas'
    }
    meta_version['usedSpecimen'] = None
    meta_version['versionIdentifier'] = 'v1'
    meta_version['versionInnovation'] = None

    space = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpace/MarmosetNMA',
        '@type': 'https://openminds.om-i.org/types/CommonCoordinateSpace',
        'abbreviation': 'MarmosetNMA',
        'author': None,
        'custodian': None,
        'description': 'The Marmoset Nencki-Monash Template is a three dimensional (3D) population-based  brain template reconstructed from 20 postmortem brains obtained from young adult marmoset monkeys (Callithrix jacchus).',
        'digitalIdentifier': None,
        'fullName': 'Marmoset Nencki-Monash Population-Based Brain Template',
        'hasVersion': [
            {
                '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMA_v1'
            }
        ],
        'homepage': 'https://www.marmosetbrain.org/nencki_monash_template',
        'howToCite': None,
        'ontologyIdentifier': None,
        'shortName': 'Marmoset Nencki-Monash Template',
        'usedSpecies': {
            '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus'
        }
    }

    space_v = space.copy()
    del space_v['hasVersion']
    del space_v['usedSpecies']
    space_v['@id'] = 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMA_v1'
    space_v['@type'] = 'https://openminds.om-i.org/types/CommonCoordinateSpaceVersion'
    space_v['abbreviation'] = 'MarmosetNMA_v1'
    space_v['accessibility'] = None
    space_v['anatomicalAxesOrientation'] = {
        '@id': 'https://openminds.om-i.org/instances/anatomicalAxesOrientation/RAS'
    }
    space_v['versionIdentifier'] = 'v1'
    space_v['versionInnovation'] = None
    space_v['fullDocumentation'] = None
    space_v['nativeUnit'] = {
        '@id': 'https://openminds.om-i.org/instances/unitOfMeasurement/millimeter'
    }
    space_v['axesOrigin'] = None
    space_v['releaseDate'] = None



    os.makedirs('brainAtlases', exist_ok=True)
    os.makedirs('brainAtlasVersions/MarmosetNMA', exist_ok=True)
    os.makedirs('commonCoordinateSpaces', exist_ok=True)
    os.makedirs('commonCoordinateSpaceVersions/MarmosetNMA', exist_ok=True)

    with open('brainAtlases/MarmosetNMA.jsonld', 'w') as f:
        f.write(json.dumps(meta, indent=4))

    with open('brainAtlasVersions/MarmosetNMA/MarmosetNMA_v1.jsonld', 'w') as f:
        f.write(json.dumps(meta_version, indent=4))

    with open('commonCoordinateSpaces/MarmosetNMA.jsonld', 'w') as f:
        f.write(json.dumps(space, indent=4))

    with open('commonCoordinateSpaceVersions/MarmosetNMA/MarmosetNMA_v1.jsonld', 'w') as f:
        f.write(json.dumps(space_v, indent=4))

async def main():
    db = Database('postgresql://monash@bqhzb5wces5.db.cloud.edu.au/marmoset')
    await db.connect()

    os.makedirs('parcellationEntities/MarmosetNMA', exist_ok=True)
    os.makedirs('parcellationEntityVersions/MarmosetNMA_v1', exist_ok=True)

    p = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@type': 'https://openminds.om-i.org/types/ParcellationEntity',
        'abbreviation': None,
        'alternateName': [
        ],
        'definition': None,
        'hasParent': None,
        'hasVersion': None,
        'name': '',
        'ontologyIdentifier': None,
        'relatedUBERONTerm': None
    }

    labels = {}
    terms = []
    term_versions = []

    area_names = {}
    with open('atlas_labels.txt', 'r') as f:
        tsv_file = csv.reader(f, delimiter='\t')
        for l in tsv_file:
            area_names[l[7]] = l[0]
    print (area_names)

    query = 'SELECT id, _3dbar_index, name, code, color_code, parent_id, center_ap, center_ml, center_dv FROM region order by _3dbar_index'
    for r in await db.fetch_all(query):
        labels[r.id] = r
        r.is_leaf = True
    #for r in await db.fetch_all(query):
    for r in labels.values():
        if r.parent_id:
            r.parent = labels[r.parent_id]
            labels[r.parent_id].is_leaf = False

    for r in labels.values():
        name = r.name.replace(',', '')
        if r.is_leaf:
            name = name[0].lower() + name[1:]
            if name not in area_names:
                print ('area_names', repr(area_names))
                raise ValueError(repr(name))
            r.name = name

    for r in labels.values():
        patt = r'\(.*?\)'
        name = r.name
        label_ids = set()
        id_ = re.sub(patt, '', r.name).strip().replace(' ', '_')
        id_ = to_camel_case(id_)
        if id_ in label_ids:
            raise ValueError('dup area code found')
        if r.parent:
            parent = r.parent
            p_id = re.sub(patt, '', parent.name).strip().replace(' ', '_')
            p_id = to_camel_case(p_id)
            p_id = f'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_{p_id}'
        label_ids.add(id_)
        code = r.code
        hex_color = r.color_code
        idx = r._3dbar_index
        p['@id'] = f'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_{id_}'
        p['hasVersion'] = [
            {
                '@id': f'https://openminds.om-i.org/instances/parcellationEntityVersion/MarmosetNMA_v1_{id_}'
            }
        ]

        p['hasParent'] = [{
            '@id': p_id
        }]
        p['abbreviation'] = code
        terms.append(p['@id'])

        p['lookupLabel'] = f'MarmosetNMA_{id_}'
        p['alternateName'] = [
        ]
        p['name'] = name
        with open(os.path.join('parcellationEntities', 'MarmosetNMA', f'MarmosetNMA_{id_}.jsonld'), 'w') as f:
            f.write(json.dumps(p, indent=4))

        pe = om.sands.ParcellationEntity.load(os.path.join('parcellationEntities', 'MarmosetNMA', f'MarmosetNMA_{id_}.jsonld'))

        print('parcellationEntity', pe.validate())
        print(pe.name)
        print()

        if r.is_leaf:
            p_v = p.copy()
            del p_v['hasVersion']
            del p_v['relatedUBERONTerm']
            del p_v['definition']
            p_v['@id'] = f'https://openminds.om-i.org/instances/parcellationEntityVersion/MarmosetNMA_v1_{id_}'
            term_versions.append(p_v['@id'])
            p_v['@type'] = 'https://openminds.om-i.org/types/ParcellationEntityVersion'
            p_v['abbreviation'] = code
            p_v['additionalRemarks'] = None
            p_v['alternateName'] = [
            ]
            p_v['correctedName'] = None
            p_v['hasAnnotation'] = [{
                '@type': 'https://openminds.om-i.org/types/AtlasAnnotation',
                'anchorPoint': None,
                'criteria': None,
                'criteriaQualityType': {
                    '@id': 'https://openminds.om-i.org/instances/criteriaQualityType/processive'
                },
                'criteriaType': {
                    '@id': 'https://openminds.om-i.org/instances/annotationCriteriaType/probabalisticAnnotation'
                },
                'inspiredBy': None,
                'internalIdentifier': f'{idx}',
                'laterality': [
                    {
                        '@id': 'https://openminds.om-i.org/instances/laterality/left'
                    },
                ],
                'preferredVisualization': {
                    '@type': 'https://openminds.om-i.org/types/ViewerSpecification',
                    'additionalRemarks': None,
                    'anchorPoint': None,
                    'cameraPosition': None,
                    'preferredDisplayColor': {
                        '@id': f'https://openminds.om-i.org/instances/singleColor/{hex_color}'
                    }
                },
                'specification': None,
                'type': None
            }]

            p_v['hasParent'] = [{
                '@id': p_id
            }]
            p_v['lookupLabel'] = f'MarmosetNMA_v1_{id_}'
            p_v['name'] = name
            p_v['ontologyIdentifier'] = None
            p_v['relationAssessment'] = None
            p_v['versionIdentifier'] = 'v1'
            p_v['versionInnovation'] = None

            with open(os.path.join('parcellationEntityVersions', 'MarmosetNMA_v1', f'MarmosetNMA_v1_{id_}.jsonld'), 'w') as f:
                f.write(json.dumps(p_v, indent=4))

            print ('loading', os.path.join('parcellationEntityVersions', 'MarmosetNMA_v1', f'MarmosetNMA_v1_{id_}.jsonld'))
            pev = om.sands.ParcellationEntityVersion.load(os.path.join('parcellationEntityVersions', 'MarmosetNMA_v1', f'MarmosetNMA_v1_{id_}.jsonld'))
        print ('done loading')

    await gen_atlas(terms, term_versions)
    await db.disconnect()

    ba = om.sands.BrainAtlas.load('brainAtlases/MarmosetNMA.jsonld')

    bav = om.sands.BrainAtlasVersion.load('brainAtlasVersions/MarmosetNMA/MarmosetNMA_v1.jsonld')

    ccs = om.sands.CommonCoordinateSpace.load('commonCoordinateSpaces/MarmosetNMA.jsonld')

    ccsv = om.sands.CommonCoordinateSpaceVersion.load('commonCoordinateSpaceVersions/MarmosetNMA/MarmosetNMA_v1.jsonld')

    print('brainAtlas', ba.validate())
    print()
    print('brainAtlasVersion', bav.validate())
    print()
    print('commonCoordinateSpace', ccs.validate())
    print()
    print('commonCoordinateSpaceVersin', ccsv.validate())

if __name__ == '__main__':
    asyncio.run(main())
