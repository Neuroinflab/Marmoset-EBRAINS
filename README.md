# Marmoset@EBRAINS Chronicles

EBRAINS is a powerful platform for advancing neuroscience, but while it provides extensive support for rodent and human research, it currently includes only one non-human primate (NHP) species. This is a significant gap, as NHPs are crucial for bridging the gap between rodent studies and human applications. To address this, our project aims to expand the platform by introducing Marmoset@EBRAINS. This initiative adds a new atlas of the marmoset (*Callithrix jacchus*) cerebral cortex, along with datasets covering neuronal distribution and cellular-level connectivity.

The atlas is built upon the [Nencki-Monash (NM)](https://doi.org/10.1016/j.neuroimage.2020.117625) template, which represents a morphological average of 20 young adult marmosets. By using Nissl histology, this template combines the fine structural details found in histology-based atlases with the high-resolution, probabilistic approach typical of MRI templates. This framework is further enriched by comprehensive maps of cortical neurons and by results from 143 experiments using fluorescent tracers to map brain connections. Additionally, we show how researchers can use existing EBRAINS tools to map their own datasets onto this new reference framework.

This work sets the stage for the marmoset to become a core model species within the EBRAINS ecosystem. By enabling more detailed cross-species comparisons and encouraging other research groups to contribute their own data, we hope to grow the EBRAINS community and make its digital tools even more versatile.

## Datasets
Throughout the project, we adjusted our approach, moving from an initial plan of three datasets to the final count of four. This change resulted from detailed discussions with the data curation team. We realized that the Nencki–Monash Atlas of the Marmoset Cerebral Cortex would be much easier to use if we presented it as two datasets. By splitting the atlas, we were able to provide the anatomical template (the underlying anatomical imaging data) independently from the parcellation (division into neuroanatomical structures). This decision ensured that both components were as clear and organized as possible. Along with these, we provided the cortico-cortical structural connectome and the whole-brain density maps of Calbindin-positive (CB+) neurons in the common marmoset.

Ultimately, these four datasets have been carefully compiled, curated, and added to the Knowledge Graph, creating a comprehensive digital map of the marmoset brain.

### Nencki-Monash Template: Average Template of the Marmoset Cortex
DOI: [10.25493/2DTR-F34](https://doi.org/10.25493/2DTR-F34).

#### Description
The [Nencki–Monash](https://doi.org/10.1016/j.neuroimage.2020.117625) (NM) template v1.0 (2020) represents a computational morphological average of 20 gender-balanced young adult brains of the common marmoset monkey (_Callithrix jacchus_), derived from 3D reconstructions based on Nissl-stained serial sections. The dataset includes a Nissl-like color anatomical reference rendered at 50 µm isotropic resolution, estimates of cortical thickness, and spatial transformations between the NM template and other selected marmoset brain templates to enhance interoperability. The template is embedded in stereotaxic coordinates, following the definition by [Paxinos et al. (2012)](https://shop.elsevier.com/books/the-marmoset-brain-in-stereotaxic-coordinates/paxinos/978-0-12-415818-4) (ISBN: [9780123978462](https://shop.elsevier.com/books/the-marmoset-brain-in-stereotaxic-coordinates/paxinos/978-0-12-415818-4)). A more comprehensive description of the template creation process is available in [Majka et. al. (2021)](https://doi.org/10.1016/j.neuroimage.2020.117625).

#### Timeline:
Data curation request: 9 January 2025  
Data descriptor submitted: 29 May 2025  
Dataset released: 3 July 2025 (175 days)

### Probabilistic Localization of Cytoarchitectural Areas of the Nencki-Monash Average Template of the Marmoset Cortex

DOI: [10.25493/RY2A-4Z1](https://doi.org/10.25493/RY2A-4Z1). 
#### Description

This document describes the probabilistic parcellation of cytoarchitectural cortical areas of the [Nencki–Monash (NM)](https://doi.org/10.1016/j.neuroimage.2020.117625) template. The NM  template represents a computational morphological average of 20 gender-balanced young adult common marmoset monkey (_Callithrix jacchus_) brains, derived from 3D reconstructions based on Nissl-stained serial sections. For a detailed description of the computational process behind the template and a comprehensive description of its components, please refer to the template data descriptor [(Majka et al., 2025)](https://doi.org/10.25493/2DTR-F34) or the original publication [Majka et al. (2021)](https://doi.org/10.1016/j.neuroimage.2020.117625).

#### Timeline:
Data curation request: 9 January 2025  
Data descriptor submitted: 25 June 2025  
Dataset released: 25 July 2025 (197 days)

### Distribution of calbindin-positive neurons across areas and layers of the marmoset cerebral cortex
DOI: [10.25493/F2GC-RYK](https://doi.org/10.25493/F2GC-RYK). 

#### Description
The dataset includes three-dimensional whole-brain density maps of neurons expressing the calcium-binding protein Calbindin (CB+) from three Common marmoset (_Callithrix jacchus_) monkeys. It also contains microscopic resolution images (×20 magnification, 0.5 µm/px) of individual immunostained sections. Quantitative estimates of CB+ densities are provided for 116 cortical areas currently recognized in the marmoset cerebral cortex, divided into supragranular, granular, and infragranular layers for each of the three individuals. The identification of CB+ neurons was performed automatically using a tailored convolutional neural network trained on the dataset examined. For each brain, the density maps, along with area and layer segmentations, are available as NIfTI files, while the high-resolution microscopic images are provided in TIFF format. Lastly, the dataset provides tabulated results in an XLSX spreadsheet.

#### Timeline:
Data curation request: 9 January 2025  
Dataset upload completed: 9 April 2025  
Dataset descriptor submitted: 6 June 2025  
Uploaded dataset validated: 13 October 2025  
Dataset released: 1 December 2025 (326 days)
