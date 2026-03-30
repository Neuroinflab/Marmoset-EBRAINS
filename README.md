# Marmoset@EBRAINS Chronicles

[EBRAINS](https://ebrains.eu/) is a powerful platform for advancing neuroscience. While it provides extensive support for rodent and human research, it currently includes only a single non-human primate (NHP) species. This is a significant shortfall, as NHPs are crucial for bridging the translational gap between rodent studies and human applications. To address this, the [Marmoset@EBRAINS](https://search.kg.ebrains.eu/instances/19810ecd-6bc4-47b8-ad6c-cd4c7a71c573?noSilentSSO=true) project aims to expand the EBRAINS platform by introducing a new atlas of the marmoset (*Callithrix jacchus*) cerebral cortex, along with datasets covering neuronal distribution maps and cellular-level connectivity.

The atlas is built upon the [Nencki-Monash (NM)](https://doi.org/10.1016/j.neuroimage.2020.117625) template, which represents a morphological average of 20 young adult marmosets. By using Nissl histology, this template combines the fine structural details found in histology-based atlases with the high-resolution, probabilistic approach typical of MRI templates. This framework is further enriched by [comprehensive maps of cortical neurons](https://doi.org/10.1371/journal.pcbi.1012428) and by results from [143 experiments](http://marmosetbrain.org) involving injections of fluorescent retrograde tracers to map [structural cortico-cortical connectivity](http://analysis.marmosetbrain.org/). Additionally, we show how researchers can use existing EBRAINS tools to map their own datasets onto this new reference framework.

This work sets the stage for the marmoset to become a core model species within the EBRAINS ecosystem. By enabling more detailed cross-species comparisons and encouraging other research groups to contribute their own data, we hope to grow the EBRAINS community and make its digital tools even more versatile.

## Datasets
Throughout the project, we adjusted our approach, moving from an initial plan of three datasets to the final count of four. This change resulted from detailed discussions with the data curation team. We realized that the Nencki–Monash Atlas of the Marmoset Cerebral Cortex would be much easier to manage if we presented it as two datasets. By splitting the atlas, we were able to provide the anatomical template (the underlying anatomical imaging data) independently from the parcellation (division into neuroanatomical structures). This decision ensured that both components were as clear and organized as possible. Along with these, we provided the cortico-cortical structural connectome and the whole-brain density maps of Calbindin-positive (CB+) neurons in the common marmoset cerebral cortex.

Ultimately, these four datasets have been carefully compiled, curated, and added to the Knowledge Graph, creating a comprehensive digital map of the marmoset brain.

### Nencki-Monash Template: Average Template of the Marmoset Cortex
DOI: [10.25493/2DTR-F34](https://doi.org/10.25493/2DTR-F34)

#### Description
The [Nencki–Monash](https://doi.org/10.1016/j.neuroimage.2020.117625) (NM) template v1.0 (2020) represents a computational morphological average of 20 gender-balanced young adult brains of the common marmoset monkey (_Callithrix jacchus_), derived from 3D reconstructions based on Nissl-stained serial sections. The dataset includes a Nissl-like color anatomical reference rendered at 50 µm isotropic resolution, estimates of cortical thickness, and spatial transformations between the NM template and other selected marmoset brain templates to enhance interoperability. The template is embedded in stereotaxic coordinates, following the definition by [Paxinos et al. (2012)](https://shop.elsevier.com/books/the-marmoset-brain-in-stereotaxic-coordinates/paxinos/978-0-12-415818-4) (ISBN: [9780123978462](https://shop.elsevier.com/books/the-marmoset-brain-in-stereotaxic-coordinates/paxinos/978-0-12-415818-4)). A more comprehensive description of the template creation process is available in [Majka et. al. (2021)](https://doi.org/10.1016/j.neuroimage.2020.117625).

#### Timeline:
Data curation request: 9 January 2025  
Data descriptor submitted: 29 May 2025  
Dataset released: 3 July 2025 (175 days)

### Probabilistic Localization of Cytoarchitectural Areas of the Nencki-Monash Average Template of the Marmoset Cortex

DOI: [10.25493/RY2A-4Z1](https://doi.org/10.25493/RY2A-4Z1)
#### Description

This document describes the probabilistic parcellation of cytoarchitectural cortical areas of the [Nencki–Monash (NM)](https://doi.org/10.1016/j.neuroimage.2020.117625) template. The NM  template represents a computational morphological average of 20 gender-balanced young adult common marmoset monkey (_Callithrix jacchus_) brains, derived from 3D reconstructions based on Nissl-stained serial sections. For a detailed description of the computational process behind the template and a comprehensive description of its components, please refer to the template data descriptor [(Majka et al., 2025)](https://doi.org/10.25493/2DTR-F34) or the original publication [Majka et al. (2021)](https://doi.org/10.1016/j.neuroimage.2020.117625).

#### Timeline:
Data curation request: 9 January 2025  
Data descriptor submitted: 25 June 2025  
Dataset released: 25 July 2025 (197 days)

### Distribution of calbindin-positive neurons across areas and layers of the marmoset cerebral cortex
DOI: [10.25493/F2GC-RYK](https://doi.org/10.25493/F2GC-RYK)

#### Description
The dataset includes three-dimensional whole-brain density maps of neurons expressing the calcium-binding protein Calbindin (CB+) from three common marmoset (_Callithrix jacchus_) monkeys. It also contains microscopic resolution images (×20 magnification, 0.5 µm/px) of individual immunostained sections. Quantitative estimates of CB+ densities are provided for 116 cortical areas currently recognized in the marmoset cerebral cortex, divided into supragranular, granular, and infragranular layers for each of the three individuals. The identification of CB+ neurons was performed automatically using a tailored convolutional neural network trained on the dataset examined. For each brain, the density maps, along with area and layer segmentations, are available as NIfTI files, while the high-resolution microscopic images are provided in TIFF format. Lastly, the dataset provides tabulated results in an XLSX spreadsheet.

#### Timeline:
Data curation request: 9 January 2025  
Dataset upload completed: 9 April 2025  
Dataset descriptor submitted: 6 June 2025  
Uploaded dataset validated: 13 October 2025  
Dataset released: 1 December 2025 (326 days)


### Cellular Resolution Cortico-Cortical Connectome of the Marmoset Monkey

DOI: [10.25493/W52W-QCU](https://doi.org/10.25493/W52W-QCU)

#### Description

This dataset presents the results of 143 injections of fluorescent retrograde tracers in 53 brain hemispheres of the common marmoset (_Callithrix jacchus_) neocortex. Data obtained from different animals are registered in a common stereotaxic space. The dataset is available in various formats, facilitating a broad range of analyses. This includes, for instance, connectivity patterns relative to cytoarchitectural areas, featuring statistical properties such as the fraction of labeled neurons and the percentage of supragranular neurons. It also provides purely spatial (parcellation-free) data based on the stereotaxic coordinates of almost 2 million labelled neurons.

#### Timeline
Data curation request: 9 January 2025  
Dataset upload completed: 14 April 2025  
Data descriptor prepared: 25 June 2025  
Accepted for the final review: 12 September 2025  
Dataset released: 8 December 2025 (334 days)

## Contribution to the EBRAINS digital atlasing infrastructure  
Expanding the platform’s capability or functionality

### Contribution to the OpenMINDS metadata framework
<!---
Adding the Marmoset NM Atlas Metadata
-->
Our primary contribution was to create and successfully merge the complete metadata definitions for the [Marmoset Nencki-Monash (NM) template](https://openminds.docs.om-i.org/en/latest/instance_libraries/anatomicalAtlasVersions/MarmosetNMA.html) and [parcellation](https://openminds.docs.om-i.org/en/latest/instance_libraries/parcellationEntities/MarmosetNMA.html) into the [`openMINDS_SANDS`](https://openminds.docs.om-i.org/en/latest/schema_specifications/SANDS.html#sands) module. This involved defining the `BrainAtlas`, `CommonCoordinateSpace`, and `ParcellationEntity` instances for a completely novel species from scratch (see [PR #303](https://github.com/openMetadataInitiative/openMINDS_instances/pull/303)).

<!---
Fixing Metadata Generation Bugs
-->
Further, while generating metadata files, we identified and patched several software bugs in the scripts. The fixes included, e.g., resolving a "double list bug" when generating `hasAnnotation` attributes, resolving problems where `IDs` were overwritten by `parent_id`, and correcting `hasParent` logic for parcellation entities.
<!---
Exposing Documentation and Validation Gaps
-->
In general, adding a new species to OpenMINDS served as a *stress test* for the platform. The Marmoset@EBRAINS project highlighted some structural gaps in the openMINDS ecosystem (e.g. [Issue #62](https://github.com/openMetadataInitiative/openMINDS/issues/62#issue-2969861157)) which emphasized the pressing need for automated validation tools so that external researchers can build and check their metadata without relying entirely on the small core curation team.

### Application of EBRAINS digital atlasing and image registration toolkit
Another contribution to the EBRAINS digital atlasing infrastructure was enabling the microscopic resolution images (0.5 µm per pixel) of the Calbindin positive (CB+) neurons through EBRAINS online tool for sharing multi-resolution images: [LocaliZoom](https://ebrains.eu/data-tools-services/tools/localizoom). In total, 457 sections images (approximately 330 gigapixels of imaging data), have been shared through the tool. A prerequisite for enabling the images via LocaliZoom was registering them to the Marmoset@EBRAINS atlas using EBRAINS digital atlasing tools: [QuickNII](https://ebrains.eu/data-tools-services/tools/quicknii) and [Visualign](https://ebrains.eu/data-tools-services/tools/visualign). This process has been carried out for all three datasets and are available under the links below:

Microscopic resolution image of Calbindin positive (CB+) neurons for:
* [Subject CJ1741](https://localizoom.apps.ebrains.eu/filmstripzoom.html?atlas=NckMnshMarmoset_50um&series=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ1741_MAPv2.json&dziproot=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ1741/&transform=.png=.tif.dzip)
* [Subject CJ200L](https://localizoom.apps.ebrains.eu/filmstripzoom.html?atlas=NckMnshMarmoset_50um&series=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ200L_mapped_MAP.json&dziproot=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ200L/&transform=.png=.tif.dzip)
* [Subject CJ205](https://localizoom.apps.ebrains.eu/filmstripzoom.html?atlas=NckMnshMarmoset_50um&series=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ205_CalB_mapped_MAP.json&dziproot=https://data-proxy.ebrains.eu/api/v1/buckets/img-69121624-98ee-4150-a09e-5e46618365/CJ205/&transform=.png=.tif.dzip)


## Dissemination of the project results

### Peer-reviewed article
Originally, we planned to prepare a peer-reviewed article quantitatively comparing the accuracy of different brain registration tools. This study was intended to use [marmoset-specific pipeline](https://doi.org/10.1002/cne.24023) from the Nencki Institute alongside species-agnostic EBRAINS software stack([QuickNii](https://ebrains.eu/data-tools-services/tools/quicknii) and [Visualign](https://ebrains.eu/data-tools-services/tools/visualign)) to map marmoset brain data and measure how precisely the tools performed.

As the project moved forward, delays in data curation and integration required more time than we initially anticipated. After consulting with the Work Package 4 coordinator, we decided to pivot away from the article to ensure we could focus on our core tasks within the project’s timeline.

Despite this change in plans, the Nencki team continued to develop the necessary technical tools for as long as the project allowed. This effort resulted in reliable methods for comparing brain segmentations and a dedicated pipeline for registering the marmoset cortex to the Nencki-Monash template. Crucially, these methods were validated against "ground truth" data—manual brain maps created by an expert neuroanatomist. These outcomes are now publicly available in the [`integration_with_ebrains_registration_toolkit`](https://github.com/Neuroinflab/Marmoset-EBRAINS/tree/integration_with_ebrains_registration_toolkit) branch of this repository.

### Abstracts and poster presentations
* **Majka P.**, Bai S., **Datta A.**, **Łabuszewska K.**, **Syc M.**, **Walkiewicz T.**, Rosa M.G.P (2026). *Expanding the EBRAINS digital atlasing ecosystem: integrating the common marmoset brain template.* Neuronus Neuroscience Forum 2026. 24th-26th April 2026, Jagiellonian University Kraków, Poland.
* **Majka P.**, Bai S., **Datta A.**, **Łabuszewska K.**, **Syc M.**, **Walkiewicz T.**, Rosa M.G.P (2025). *Bringing Marmoset to EBRAINS. 17th International Congress of the Polish Neuroscience Society*, Wrocław, 2nd-5th September 2025, poster no. [P2.45](https://ptbun.org.pl/base/abstracts_view.php?a=show&no=9176171382) ([see the poster](https://pmajka.github.io/2025-08-26-pns-ebrains-poster.jpg)).

### Talks and presentations
* **Majka P.** (2025) *Getting the marmoset aboard EBRAINS - a case study*. User talk at EBRAINS Summit, 10th December 2025, Brussels, Belgium (invited speaker).
* **Majka P.** (2025). *Digital neuroanatomy, why and how? Cortico-cortical connectivity atlas of the common marmoset (Callithrix jacchus)*. Flash talk at PRIMatE Resource Exchange (PRIME-RE) Global Collaboration Forum, 4th–5th December 2025, online meeting.
* **Majka P.** (2025). *Bringing Marmoset to EBRAINS (Marmoset@EBRAINS)*. EBRAINS Co-Design meeting, 10th June 2025, online meeting (invited speaker).
* **Majka P.** (2025). *Digital neuroanatomy, why and how? 17th International Congress of the Polish Neuroscience Society*, Wrocław, 3rd September 2025 (invited speaker during a plenary session).

### Press releases and interviews
19th February 2026
* https://ebrains.eu/news-and-events/2026/new-marmoset-brain-atlas-added-to-ebrains
* https://x.com/EBRAINS_eu/status/2024500316444479804
* https://www.linkedin.com/feed/update/urn:li:activity:7430266127756230656
* https://mastodon.social/@ebrains/116097914748192558
* https://bsky.app/profile/ebrains.bsky.social/post/3mf7ulwkjj22s

22nd December 2025
* https://ebrains.eu/data-tools-services/brain-atlases/marmoset-brain-atlas

20 March 2025
* https://ebrains.eu/news-and-events/2025/four-new-open-call-projects-will-contribute-with-large-datasets-and-new

### Abstracts

#### 17th International Congress of the Polish Neuroscience Society,  Wrocław, 2-5 September 2025 abstract
[P2.45. BRINGING MARMOSET TO EBRAINS](https://ptbun.org.pl/base/abstracts_view.php?a=show&no=9176171382)

Piotr Majka (1,2), Shi Bai (2), Adam Datta (1), Karolina Łabuszewska (1), Marcin Syc (1), Tomasz Walkiewicz (1), Marcello G. P. Rosa (2)  

(1) Laboratory of Neuroinformatics, Nencki Institute of Experimental Biology of the Polish Academy of Sciences, 02-093 Warsaw, Poland  
(2) Biomedicine Discovery Institute and Department of Physiology, Monash University, Clayton, VIC 3800, Australia

**INTRODUCTION**: EBRAINS is one of the most potent platforms for advancing neuroscience research. While it provides extensive support for rodent (predominantly mouse) and human-oriented datasets, it currently supports only one non-human primate (NHP) species despite the critical role of NHPs in bridging the translational gap between rodent and human studies.

**AIM(S)**: To address this limitation, we propose to expand the EBRAINS platform by incorporating a new atlas of the marmoset (Callithrix jacchus) cerebral cortex, which we will call Marmoset@EBRAINS. This atlas will be accompanied by diverse datasets such as neuronal distribution and cellular-level connectivity registered to this new reference framework.

**METHOD(S)**: The proposed atlas will be derived from the Nencki-Monash marmoset brain template (NM template), a gender-balanced, morphological average of 20 young adult marmosets. Based on Nissl histology, the template combines the detailed cytoarchitectural information of histology-based atlases with the isotropic resolution and probabilistic analyses typical of MR-based templates. We will then complement the new framework with multimodal datasets, including comprehensive maps of neuronal distribution in the cortex and results from 143 experiments investigating cortical area connections using fluorescent tracers. Additionally, we will demonstrate how EBRAINS users can map their datasets onto the Marmoset@EBRAINS atlas using existing EBRAINS digital atlasing tools.

**CONCLUSIONS**: This project will lay the groundwork for the broad integration of the marmoset as a model species within EBRAINS. The project will directly benefit the EBRAINS initiative by enabling more extensive cross-species analyses and encouraging other marmoset research groups to integrate their datasets with the new framework, thereby expanding the user base. It also represents a significant step towards generalising the available atlasing tools, enhancing the platform's versatility.

**FINANCIAL SUPPORT**: This project is co-funded by the European Union's Horizon Europe Research Infrastructures programme under grant agreement no. 101147319 (EBRAINS 2.0) and by the National Science Centre (2019/35/D/NZ4/03031).

#### EBRAINS Summit 2025 – Transforming Brain Research and Medicine – Brussels on 8-11 December.
[User talk: Bringing Marmoset to EBRAINS](https://summit2025.ebrains.eu/programme/user-talk-bringing-marmoset-to-ebrains)

Piotr Majka (1)

(1) Laboratory of Neuroinformatics, Nencki Institute of Experimental Biology of the Polish Academy of Sciences, 02-093 Warsaw, Poland


The [Marmoset@EBRAINS project](https://search.kg.ebrains.eu/instances/19810ecd-6bc4-47b8-ad6c-cd4c7a71c573?noSilentSSO=true) focused on expanding the EBRAINS research infrastructure by incorporating a digital atlas of the common marmoset brain. This effort is driven by the marmoset's growing importance as a primate model for bridging the translational gap between human and rodent studies in neuroscience. At the same time, the project serves as a real-world test of the platform's core principles: flexibility, interoperability, and extensibility.


#### NEURONUS & Young PTBUN Neuroscience Forum Krakow, 24-26 April 2026 Abstract
#### Expanding the EBRAINS digital atlasing ecosystem: integrating the common marmoset brain template

Piotr Majka (1,2), Shi Bai (2), Adam Datta (1), Karolina Łabuszewska (1), Marcin Syc (1), Tomasz Walkiewicz (1), Marcello G. P. Rosa (2)  

(1) Laboratory of Neuroinformatics, Nencki Institute of Experimental Biology of the Polish Academy of Sciences, 02-093 Warsaw, Poland  
(2) Biomedicine Discovery Institute and Department of Physiology, Monash University, Clayton, VIC 3800, Australia

EBRAINS is a leading platform for advancing neuroscience research, providing extensive support for rodent and human-oriented datasets. However, it currently supports only one non-human primate (NHP) species, despite the critical role NHPs play in bridging the transnational gap between rodent models and human studies. From a technical standpoint, the platform lacks a standardized procedure for incorporating atlases of additional animal species.

To address this limitation, we propose extending the EBRAINS platform by integrating an atlas of the common marmoset brain, termed [Marmoset@EBRAINS project](https://search.kg.ebrains.eu/instances/19810ecd-6bc4-47b8-ad6c-cd4c7a71c573?noSilentSSO=true). The atlas is accompanied with additional datasets, including neuronal distribution and cellular-level connectivity. Additionally, we demonstrate how EBRAINS users can map their own datasets onto the atlas using the platform's digital atlasing tools.

The proposed atlas is derived from the [Nencki-Monash](https://doi.org/10.1016/j.neuroimage.2020.117625) marmoset brain template, a morphological average of 20 marmoset brains. The template combines high-resolution cytoarchitectural information with the isotropic resolution of MR-based templates. The atlas is implemented via [Siibra-Explorer](https://atlases.ebrains.eu/viewer/#/a:nencki:nm:atlas:v1.0.0:marmoset/t:nencki:nm:referencespace:v1.0.0:MARMOSET_NM_NISSL_2020/p:nencki:nm:parcellationatlas:v1.0.0:MARMOSET_NM/@:0.0.0.-W000.._eCwg.2-FUe3._-s_W.2_evlu..16PF..0.0.0..CqK/vs:v2-ff011b0b), the native EBRAINS atlas browser, while accompanying datasets were curated using the OpenScienceData workflow.

We implemented the Marmoset@EBRAINS atlas as a hosted resource on the platform. To facilitate this integration, we also extended the Siibra-Explorer plugin system to support features specific to our atlas. Further, we provided four curated, FAIR-compliant datasets that are fully integrated into the EBRAINS Knowledge Graph and registered with the openMINDS metadata framework.

This project lays the foundation for integrating the marmoset as a model species within EBRAINS. By providing a framework that enables other research groups to contribute data, it substantially broadens the platform’s potential user base. Finally, this work marks an important step toward generalizing EBRAINS’ atlasing tools and increasing the platform’s versatility.

Financial Support 

EBRAINS 2.0 (101147319, Financial Support to Third Parties, FSTP)
