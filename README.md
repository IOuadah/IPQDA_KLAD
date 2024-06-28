# From darkness to light: a quantitative image analysis original. 

#Abstract
In this project we focused on establishing a comprehensive image analysis pipeline using Python that included, cell segmentation, training a cellpose model, measuring the intensity and eventually tracking the movement of the cells. We compared the custom model with the pretrained model that cellpose provides. The segmentation was done using cellpose and the tracking was performed using trackmate. The results of this research was that the ...model resulted in more acurate segmentation than the ... model. 

#Introduction
The innovations in the field of single cell technologies have made it possible to perform high-throughput profiling of many different celltypes. This causes an enormeous increase of data that needs to be processed accordingly. Therefore, establishing a comprehensive pipeline is of the essence in these cases. Python is a useful tool to enable this aim. Therefore in this paper we aimed to produce a comprehensive pipeline for single cell image analysis using Python. Considering that we use images as our data source the overall pipeline consisted of several tasks. Namely, cellsegmentation, training a cellpose model, measuring the intensity of the protein of interest and other cell components and finally celltracking. The data consisted of images obtained by a high-resolution confocal microscope (90 nm x 90 nm pixels, 1024x1024 image size). The cells that were used were probed with fluorescent markers: one for the protein of interest β-catenin (green) and for the nuclei (red). 
