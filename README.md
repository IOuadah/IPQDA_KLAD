# From darkness to light: a quantitative image analysis original. 

**#Abstract**\
In this project we focused on establishing a comprehensive image analysis pipeline using Python that included, cell segmentation, training a cellpose model, measuring the intensity and eventually tracking the movement of the cells. We compared the custom model with the pretrained model that cellpose provides. The segmentation was done using cellpose and the tracking was performed using trackmate. The results of this research was that the ...model resulted in more acurate segmentation than the ... model. 

**#Introduction**\
The innovations in the field of single cell technologies have made it possible to perform high-throughput profiling of many different celltypes (https://www.nature.com/articles/s41576-023-00586-w ). This causes an enormeous increase of data that needs to be processed accordingly. Therefore, establishing a comprehensive pipeline is of the essence in these cases. Python is a useful tool to enable this aim. Therefore in this paper we aimed to produce a comprehensive pipeline for single cell image analysis using Python. Considering that we use images as our data source the overall pipeline consisted of several tasks. Namely, cellsegmentation, training a cellpose model, measuring the intensity of the protein of interest and other cell components and finally celltracking. The data consisted of images obtained by a high-resolution confocal microscope (90 nm x 90 nm pixels, 1024x1024 image size). The cells that were used were probed with fluorescent markers: one for the protein of interest β-catenin (green) and for the nuclei (red). \

β-catenin is a protein that is involved in cell-cell interactions, it is therefore found in the cell boundaries. However, β-catenin also plays a role in gene regulation, which causes an increase of the protein in the cytoplasm and in the nucleus. This increase can be experimentally induced by using a specific drug that inhibits β-catenin degradation or by inducing the so-called Wnt pathway using Wnt ligands. \

The data consisted of a control dataset, this resembles the "normal" situation without stimulation and a sample dataset which is the situation with stimulation. The aim of this pipeline is to measure the average fluorescence intensity of β-catenin across three different compartements, namely the nucleus, the cytoplasm and the cell boundary. To accomplish this, accurate segmentation of both of the channels was essential. To handle the complex shapes of the cells and the varying intensity contrasts of the cells and nuclei, we used the robust Cellpose. Cellpose is a deeplearning based method that is written in Python. It has a useful API, which also allows for training of custom models based on user data. We used this to train our own segmentation model, to improve the accuracy of segmentation. Using these segmentated masks, we calculated the measurement masks of the different compartements to eventually measure the average fluorescence intensity. 

**#Results**\
TASK 2 
In this task, we have used the cellpose API to perform segmentation by using the pre-trained models (cyto2 and nuclei). This task focused on generating and analyzing outline images and masks (cytoplasm and nuclei) to evaluate the quality of the segmentation.

**Plot**

**Plot description**
-	Laat de outlines en masks zien voor beide channels
-	Zeg iets over de kwaliteit van de segmentation, welke plekken zijn gemist enzo
-	Maybe een gif maar skip dat sorry

TASK 3 Next, we had to create a training dataset for the segmentation of the cytoplasm and nuclei by manually correcting the segmentation labels for a subset of images. The goal is to prepare high-quality training data for improving segmentation models. For each dataset (control and sample) we selected 8 images for both channels, in total we manually inspected 32 images. WELKE EN WRM We did this in ImageJ with the help of the provided macros. The manually corrected images help in improving the accuracy of the segmentation and to better train the model.

**Plots**

**Explain before and afters**

Task 4: Training the custom cellpose models. 
To improve the segmentation accuracy, we trained custom cellpose models for the cytoplasm and the nuclei. This was established by choosing 8 images from each dataset (control and sample) for both the cytoplasm and the nucleus, eventually ending up with 32 images. The 8 images were selected by using intervals of 10, this was done to keep the temporal tendencies in the dataset. The selected images  underwent manually improving of the pre-trained segmentation to ensure high quality training data. The manual editing was done in FIJI. /

The model's training parameters:/
Epochs: /
Batch size: /
Learning rate: /

After training, the training data was segmented using the custom models and compared to the result obtained from the pretrained models. This resulted for the cytoplasm model a more accurate boundary detection and cell shapes and for the nucleus model a better handling of overlapping nuclei. /


The new version of the Fiji plugin called TrackMate offers a comprehensive suite of tools to perform tracking, data visualization, track analysis in an efficient and user-friendly manner. This versatile tool facilitates the tracking of single cells viewed with fluorescence microscopes, making it an essential tool for biological research  (Tinevez et al., 2017).

Using TrackMate, researchers are able to track the movements and behaviors of individual cells, providing crucial insight into various physiological processes (Fazeli et al., 2020).

Contributions

References/sources

