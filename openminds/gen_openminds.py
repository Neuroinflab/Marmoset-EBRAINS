import os
import types
import re
import json
import csv
import operator

import asyncio

import msgpack
from databases import Database

import openminds.latest as om

def to_camel_case(text):
    print ('===== from =====', text)
    text = text[0].lower() + text[1:]
    res = re.sub(r"[_]([a-zA-Z0-9])", lambda x: x[1].upper(), text)

    print ('===== to =====', res)
    return res

async def gen_atlas(terms, term_versions):
    print ('terms', sorted(terms))
    atlas = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@id': 'https://openminds.om-i.org/instances/brainAtlas/MarmosetNMA',
        '@type': 'https://openminds.om-i.org/types/BrainAtlas',
        'abbreviation': 'MarmosetNMA',
        'author': None,
        'custodian': None,
        'description': 'The Marmoset Nencki-Monash Atlas is a three dimensional (3D) probabilistic brain atlas reconstructed from 20 young adult marmoset monkeys (Callithrix jacchus) and segmented based on the cytoarchitectonic analysis of the serial Nissl-stained sections of those brains.',
        'digitalIdentifier': None,
        'fullName': 'Marmoset Nencki-Monash Probabilistic Cytoarchitectonic Brain Atlas',
        'ontologyIdentifier': None,
        'hasTerminology': {
            '@type': 'https://openminds.om-i.org/types/ParcellationTerminology',
            'dataLocation': None,
            'hasEntity': [{'@id': t} for t in sorted(terms)],
            'ontologyIdentifier': None,
        },
        'hasVersion': [{
            '@id': 'https://openminds.om-i.org/instances/brainAtlasVersion/MarmosetNMA_v1'
        }],
        'homepage': 'https://www.marmosetbrain.org/',
        'howToCite': 'Please refer to the atlas by its [RRID:SCR_018367](https://scicrunch.org/resolver/SCR_018367), and cite the publication of the version of the template you have used.',
        'shortName': 'Marmoset Nencki-Monash Atlas',
        'usedSpecies': {
            '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus'
        }
    }
    atlas_version = atlas.copy()
    del atlas_version['hasVersion']
    del atlas_version['usedSpecies']
    atlas_version['@id'] = 'https://openminds.om-i.org/instances/brainAtlasVersion/MarmosetNMA_v1'
    atlas_version['@type'] = 'https://openminds.om-i.org/types/BrainAtlasVersion'
    atlas_version['accessibility'] = {
        '@id': 'https://openminds.om-i.org/instances/productAccessibility/freeAccess'
    }
    atlas_version['coordinateSpace'] = {
        '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1'
    }
    atlas_version['copyright'] = None
    atlas_version['fullDocumentation'] = None
    atlas_version['funding'] = None
    atlas_version['hasTerminology'] = {
        '@type': 'https://openminds.om-i.org/types/ParcellationTerminologyVersion',
        'dataLocation': None,
        'hasEntity': [{'@id': t} for t in sorted(term_versions)],
        'ontologyIdentifier': None
    }

    atlas_version['isAlternativeVersionOf'] = None
    atlas_version['isNewVersionOf'] = None
    atlas_version['keyword'] = None
    atlas_version['license'] = {
        '@id': 'https://openminds.om-i.org/instances/licenses/CC-BY-4.0'
    }
    atlas_version['majorVersionIdentifier'] = None
    atlas_version['ontologyIdentifier'] = None
    atlas_version['otherContribution'] = None
    atlas_version['relatedPublication'] = [{
        '@id': 'https://doi.org/10.1016/j.neuroimage.2020.117625'
    }]
    atlas_version['releaseDate'] = '2021-02-01'
    atlas_version['repository'] = None
    atlas_version['supportChannel'] = [
        'support@marmosetbrain.org'
    ]
    atlas_version['type'] = {
        '@id': 'https://openminds.om-i.org/instances/atlasType/probabilisticAtlas'
    }
    atlas_version['usedSpecimen'] = None
    atlas_version['versionIdentifier'] = 'v1'
    atlas_version['versionInnovation'] = 'This is the first version of this atlas.'
    atlas_version['fullDocumentation'] = {
        '@id': 'https://www.marmosetbrain.org/nencki_monash_template'
    }
    atlas_version['author'] = None
    atlas_version['custodian'] = None
    atlas_version['description'] = None
    atlas_version['digitalIdentifier'] = None
    atlas_version['copyright'] = None
    atlas_version['howToCite'] = 'Majka, P., Bednarek, S., Chan, J. M., Jermakow, N., Liu, C., Saworska, G., Worthy, K. H., Silva, A. C., Wójcik, D. K., & Rosa, M. G. P. (2021). Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas. NeuroImage, 226, 117625. https://doi.org/10.1016/j.neuroimage.2020.117625.'
    space1 = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpace/P-MarmosetBSC-corT',
        '@type': 'https://openminds.om-i.org/types/CommonCoordinateSpace',
        'abbreviation': 'P-MarmosetBSC-corT',
        'author': None,
        'description': 'Stereotactic coordinate space of the coronal plane.',
        'custodian': None,
        'digitalIdentifier': None,
        'fullName': 'Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates',
        'hasVersion': [
            {
                '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/P-MarmosetBSC-corT_v2012-Interaural-LSA'
            }
        ],
        'homepage': 'http://www.neura.edu.au/research/themes/paxinos-group',
        'howToCite': None,
        'ontologyIdentifier': None,
        'shortName': 'Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)',
        'usedSpecies': {
            '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus'
        }
    }

    space1_v = space1.copy()
    del space1_v['hasVersion']
    del space1_v['usedSpecies']
    space1_v['@id'] = 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/P-MarmosetBSC-corT_v2012-Interaural-LSA'
    space1_v['@type'] = 'https://openminds.om-i.org/types/CommonCoordinateSpaceVersion'
    space1_v['accessibility'] = {
        '@id': 'https://openminds.om-i.org/instances/productAccessibility/freeAccess'
    }
    space1_v['anatomicalAxesOrientation'] = {
        '@id': 'https://openminds.om-i.org/instances/anatomicalAxesOrientation/LSA'
    }
    space1_v['versionIdentifier'] = 'v2012 (Interaural, LSA)'
    space1_v['fullDocumentation'] = {
        '@id': 'https://openminds.om-i.org/instances/ISBN/978-0-12-415818-4'
    }
    space1_v['nativeUnit'] = {
        '@id': 'https://openminds.om-i.org/instances/unitOfMeasurement/millimeter'
    }
    space1_v['axesOrigin'] = None
    space1_v['releaseDate'] = '2011-10-11'
    space1_v['copyright'] = None
    space1_v['usedSpecimen'] = None
    """
    [
        {
            '@type': 'https://openminds.om-i.org/types/Subject',
            'species': {
                '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus',
            },
            'studiedState': [{
                '@type': 'https://openminds.om-i.org/types/SubjectState',
                'ageCategory': {
                    '@id': 'https://openminds.om-i.org/instances/ageCategory/youngAdult',
                },
                'age': {
                    '@type': 'https://openminds.om-i.org/types/QuantitativeValue',
                    'typeOfUncertainty': None,
                    'uncertainty': None,
                    'value': '3.16',
                    'unit': {
                        '@id': 'https://openminds.om-i.org/instances/unitOfMeasurement/year'
                    }
                },
                'weight': {
                    '@type': 'https://openminds.om-i.org/types/QuantitativeValue',
                    'typeOfUncertainty': None,
                    'uncertainty': None,
                    'value': '500',
                    'unit': {
                        '@id': 'https://openminds.om-i.org/instances/unitOfMeasurement/gram'
                    }
                }
            }],
            'biologicalSex': {
                '@id': 'https://openminds.om-i.org/instances/biologicalSex/female'
            },
        }
    ]
    """
    space1_v['versionInnovation'] = 'This is the first version of this stereotaxic coordinate system.'
    space1_v['digitalIdentifier'] = None
    space1_v['homepage'] = 'http://www.neura.edu.au/research/themes/paxinos-group'
    space1_v['isNewVersionOf'] = None
    space1_v['otherContribution'] = None
    space1_v['supportChannel'] = None
    space1_v['defaultImage'] = None
    space1_v['funding'] = None
    space1_v['isAlternativeVersionOf'] = None
    space1_v['repository'] = None
    space1_v['relatedPublication'] = None
    space1_v['keyword'] = None
    space1_v['license'] = None
    space1_v['description'] = 'This coordinate space of the coronal plates from Paxinos et al. \'Marmoset Brain in Stereotaxic Coordinates\' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the marmoset brain could not be determined from the information provided in the atlas publication. This coordinate space has LSA orientation (X, Y, Z axes are oriented towards left, superior and anterior, respectively). This was obtained by combining information provided in the pdf version of the 1st edition: (1) "In the common marmoset, the horizontal zero plane is defined as the plane passing thorough the lower margin of the orbit and the center of the external auditory meatus (Figure B). The anteroposterior zero plane is defined as the plane perpendicular to the horizontal zero plane which passes the centers of the external auditory meati. The left-right zero plane is the midsagittal plane [...]." (quoted from chapter \'Introduction\', subsection \'Histology\', page IX). (2) Based on Figure C (chapter \'Introduction\', subsection \'Histology\', page X), the fiducial marks were made on the right hemisphere of the marmoset brain. These are visible in some of the photographic plates (e.g., Figure 187a) identifying the left hemisphere as delineated one. Thus, the coordinate system is oriented towards the left since the marmoset\'s left hemisphere has been used to draw the atlas. A pdf version of the atlas can be accessed from https://r.marmosetbrain.org/Atlas+Small.pdf or https://www.researchgate.net/publication/335871101_PDF_of_The_Marmoset_Brain_in_Stereotaxic_Coordinates.'

    space2 = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpace/MarmosetNMT',
        '@type': 'https://openminds.om-i.org/types/CommonCoordinateSpace',
        'abbreviation': 'MarmosetNMT',
        'author': None,
        'custodian': None,
        'description': 'Stereotactic coordinate space of the coronal plane generated using computational average of histology sections.',
        #'digitalIdentifier': {
        #    '@id': 'https://scicrunch.org/resolver/RRID:SCR_018367'
        #},
        'digitalIdentifier': None,
        'fullName': 'The Marmoset Nencki-Monash Template in Stereotaxic Coordinates',
        'hasVersion': [
            {
                '@id': 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1'
            }
        ],
        'homepage': 'https://www.marmosetbrain.org/nencki_monash_template',
        'howToCite': 'Please refer to the template by its RRID:SCR_018367, and cite the publication of the version of the template you have used.',
        #'howToCite': 'Majka, P., Bednarek, S., Chan, J. M., Jermakow, N., Liu, C., Saworska, G., Worthy, K. H., Silva, A. C., Wójcik, D. K., & Rosa, M. G. P. (2021). Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas. NeuroImage, 226, 117625. https://doi.org/10.1016/j.neuroimage.2020.117625',
        'ontologyIdentifier': None,
        'shortName': 'Marmoset Nencki-Monash Template',
        'usedSpecies': {
            '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus'
        }
    }

    space2_v = space2.copy()
    del space2_v['hasVersion']
    del space2_v['usedSpecies']
    del space2_v['digitalIdentifier']
    space2_v['@id'] = 'https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1'
    space2_v['@type'] = 'https://openminds.om-i.org/types/CommonCoordinateSpaceVersion'
    space2_v['abbreviation'] = 'MarmosetNMT'
    space2_v['accessibility'] = {
        '@id': 'https://openminds.om-i.org/instances/productAccessibility/freeAccess'
    }
    space2_v['anatomicalAxesOrientation'] = {
        '@id': 'https://openminds.om-i.org/instances/anatomicalAxesOrientation/LPI'
    }
    space2_v['versionIdentifier'] = 'v1'
    space2_v['fullDocumentation'] = {
        '@id': 'https://www.marmosetbrain.org/nencki_monash_template/'
    }
    space2_v['nativeUnit'] = {
        '@id': 'https://openminds.om-i.org/instances/unitOfMeasurement/millimeter'
    }
    space2_v['axesOrigin'] = None

    space2_v['releaseDate'] = '2021-02-01'
    space2_v['copyright'] = None
    space2_v['usedSpecimen'] = None
    """
    [
        {
            '@type': 'https://openminds.om-i.org/types/SubjectGroup',
            'species': {
                '@id': 'https://openminds.om-i.org/instances/species/callithrixJacchus',
            },
            'studiedState': [{
                '@type': 'https://openminds.om-i.org/types/SubjectGroupState',
                'ageCategory': [{
                    '@id': 'https://openminds.om-i.org/instances/ageCategory/youngAdult',
                }],
            }],
            'numberOfSubjects': 20,
            'biologicalSex': [{
                '@id': 'https://openminds.om-i.org/instances/biologicalSex/male'
            }, {
                '@id': 'https://openminds.om-i.org/instances/biologicalSex/female'
            }],
        }
    ]
    """
    space2_v['versionInnovation'] = 'This is the first version of average histology.'
    space2_v['homepage'] = 'https://www.marmosetbrain.org/nencki_monash_template'

    space2_v['isNewVersionOf'] = None
    space2_v['otherContribution'] = None
    space2_v['supportChannel'] = None
    space2_v['defaultImage'] = None
    space2_v['funding'] = None
    space2_v['isAlternativeVersionOf'] = None
    space2_v['repository'] = None
    space2_v['relatedPublication'] = [
        {
            '@id': 'https://doi.org/10.1016/j.neuroimage.2020.117625'
        }
    ]
    space2_v['keyword'] = None
    space2_v['license'] = {
        '@id': 'https://openminds.om-i.org/instances/licenses/CC-BY-4.0'
    }
    space2_v['description'] = 'The Nencki-Monash (NM) template v1.0 (2020) represents a computational morphological average of selected gender-balanced young adult brains of the Common Marmoset monkey (Callithrix jacchus), derived from 3D reconstructions based on Nissl-stained serial sections.'
    space2_v['howToCite'] = 'Majka, P., Bednarek, S., Chan, J. M., Jermakow, N., Liu, C., Saworska, G., Worthy, K. H., Silva, A. C., Wójcik, D. K., & Rosa, M. G. P. (2021). Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas. NeuroImage, 226, 117625. https://doi.org/10.1016/j.neuroimage.2020.117625.'

    os.makedirs('brainAtlases', exist_ok=True)
    os.makedirs('brainAtlasVersions/MarmosetNMA', exist_ok=True)
    os.makedirs('commonCoordinateSpaces', exist_ok=True)
    os.makedirs('commonCoordinateSpaceVersions/MarmosetNMT', exist_ok=True)
    os.makedirs('commonCoordinateSpaceVersions/P-MarmosetBSC-corT', exist_ok=True)

    with open('brainAtlases/MarmosetNMA.jsonld', 'w') as f:
        f.write(json.dumps(atlas, sort_keys=True, indent=2, ensure_ascii=False) + '\n')

    with open('brainAtlasVersions/MarmosetNMA/MarmosetNMA_v1.jsonld', 'w') as f:
        f.write(json.dumps(atlas_version, sort_keys=True, indent=2, ensure_ascii=False) + '\n')

    with open('commonCoordinateSpaces/P-MarmosetBSC-corT.jsonld', 'w') as f:
        f.write(json.dumps(space1, sort_keys=True, indent=2) + '\n')

    with open('commonCoordinateSpaces/MarmosetNMT.jsonld', 'w') as f:
        f.write(json.dumps(space2, sort_keys=True, indent=2, ensure_ascii=False) + '\n')

    with open('commonCoordinateSpaceVersions/P-MarmosetBSC-corT/P-MarmosetBSC-corT_v2012-Interaural-LSA.jsonld', 'w') as f:
        f.write(json.dumps(space1_v, sort_keys=True, indent=2) + '\n')

    with open('commonCoordinateSpaceVersions/MarmosetNMT/MarmosetNMT_v1.jsonld', 'w') as f:
        f.write(json.dumps(space2_v, sort_keys=True, indent=2, ensure_ascii=False) + '\n')

async def main():
    db = Database('postgresql://monash:marmosetConnectome@bqhzb5wces5.db.cloud.edu.au/marmoset')
    await db.connect()

    os.makedirs('parcellationEntities/MarmosetNMA', exist_ok=True)
    os.makedirs('parcellationEntityVersions/MarmosetNMA_v1', exist_ok=True)

    p = {
        '@context': {
            '@vocab': 'https://openminds.om-i.org/props/'
        },
        '@type': 'https://openminds.om-i.org/types/ParcellationEntity',
        'abbreviation': None,
        'alternateName': None,
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
        print (repr(r))
        labels[r.id] = r
        r.is_leaf = True
    #for r in await db.fetch_all(query):
    for r in labels.values():
        if r.parent_id:
            r.parent = labels[r.parent_id]
            labels[r.parent_id].is_leaf = False
    labels[2643].is_leaf = False

    brain = types.SimpleNamespace()
    brain.id = 0
    brain._3dbar_index = 66
    brain.name = 'Brain'
    brain.comma_name = 'Brain'
    brain.code = 'Brain'
    brain.color_code = '#666666'
    brain.parent_id = None
    brain.parent = None
    brain.is_leaf = False
    labels[2623].parent = brain
    labels[0] = brain
    for r in labels.values():
        comma_name = r.name
        name = r.name.replace(',', '')
        if r.is_leaf:
            comma_name = comma_name[0].lower() + comma_name[1:]
            name = name[0].lower() + name[1:]
            if name not in area_names:
                print ('area_names', repr(area_names))
                raise ValueError(repr(name))
            r.comma_name = comma_name
            r.name = name

    for r in labels.values():
        patt = r'\(.*?\)'
        multiple_ws = r' +'
        name = r.name
        label_ids = set()
        id_ = re.sub(patt, '', r.name).strip()
        id_ = re.sub(multiple_ws, ' ', id_)
        id_ = id_.replace(' ', '_')
        id_ = to_camel_case(id_)
        if id_ in label_ids:
            raise ValueError('dup area code found')
        if r.parent:
            parent = r.parent
            p_id = re.sub(patt, '', parent.name).strip()
            p_id = re.sub(multiple_ws, ' ', p_id)
            p_id = p_id.replace(' ', '_')
            p_id = to_camel_case(p_id)
            p_id = f'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_{p_id}'
        label_ids.add(id_)
        code = r.code
        hex_color = r.color_code
        idx = r._3dbar_index
        p['@id'] = f'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_{id_}'
        if r.is_leaf:
            p['hasVersion'] = [
                {
                    '@id': f'https://openminds.om-i.org/instances/parcellationEntityVersion/MarmosetNMA_v1_{id_}'
                }
            ]
        else:
            p['hasVersion'] = None

        if r.parent:
            p['hasParent'] = [{
                '@id': p_id
            }]
        else:
            p['hasParent'] = None

        p['abbreviation'] = code
        if p['@id'] not in terms:
            terms.append(p['@id'])

        p['lookupLabel'] = f'MarmosetNMA_{id_}'
        if r.comma_name == r.name:
            p['alternateName'] = None
        else:
            p['alternateName'] = [
                r.comma_name
            ]
        p['name'] = name
        extra = ''
        if idx == 101:
            continue
        if idx == 100:
            p['hasParent'] = [{
                '@id': 'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_ventralPallium'
            }]

        with open(os.path.join('parcellationEntities', 'MarmosetNMA', f'MarmosetNMA_{id_}{extra}.jsonld'), 'w') as f:
            f.write(json.dumps(p, sort_keys=True, indent=2) + '\n')

        if r.is_leaf:
            p_v = p.copy()
            del p_v['hasVersion']
            del p_v['relatedUBERONTerm']
            del p_v['definition']
            p_v['@id'] = f'https://openminds.om-i.org/instances/parcellationEntityVersion/MarmosetNMA_v1_{id_}'
            term_versions.append(p_v['@id'])
            p_v['@type'] = 'https://openminds.om-i.org/types/ParcellationEntityVersion'
            #p_v['abbreviation'] = code
            p_v['additionalRemarks'] = None
            #p_v['alternateName'] = None
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
                        '@id': f'https://openminds.om-i.org/instances/colormap/matplotlib.colormaps.Greys'
                    },
                },
                'specification': None,
                'type': {
                    '@id': 'https://openminds.om-i.org/instances/annotationType/annotationMask'
                }
            }, {
                '@type': 'https://openminds.om-i.org/types/AtlasAnnotation',
                'anchorPoint': None,
                'criteria': None,
                'criteriaQualityType': {
                    '@id': 'https://openminds.om-i.org/instances/criteriaQualityType/processive'
                },
                'criteriaType': {
                    '@id': 'https://openminds.om-i.org/instances/annotationCriteriaType/deterministicAnnotation'
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
                'type': {
                    '@id': 'https://openminds.om-i.org/instances/annotationType/annotationMask'
                }

            }]

            p_v['hasParent'] = [{
                '@id': p_id
            }]
            if idx == 100:
                p_v['hasParent'] = [{
                    '@id': 'https://openminds.om-i.org/instances/parcellationEntity/MarmosetNMA_ventralPallium'
                }]
            p_v['lookupLabel'] = f'MarmosetNMA_v1_{id_}'
            p_v['name'] = name
            p_v['ontologyIdentifier'] = None
            p_v['relationAssessment'] = None
            p_v['versionIdentifier'] = 'v1'
            p_v['versionInnovation'] = 'This is the first version of this parcellation entity.'

            with open(os.path.join('parcellationEntityVersions', 'MarmosetNMA_v1', f'MarmosetNMA_v1_{id_}.jsonld'), 'w') as f:
                f.write(json.dumps(p_v, sort_keys=True, indent=2) + '\n')


    await gen_atlas(terms, term_versions)
    await db.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
