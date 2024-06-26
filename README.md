# From darkness to light: a quantitative image analysis original. 

**#Abstract**\
In this project we focused on establishing a comprehensive image analysis pipeline using Python that included, cell segmentation, training a cellpose model, measuring the intensity and eventually tracking the movement of the cells. We compared the custom model with the pretrained model that cellpose provides. The segmentation was done using cellpose and the tracking was performed using trackmate. The results of this research was that the ...model resulted in more acurate segmentation than the ... model. 

**#Introduction**\
The innovations in the field of single cell technologies have made it possible to perform high-throughput profiling of many different celltypes (Heumos et al., 2023). This causes an enormeous increase of data that needs to be processed accordingly. Therefore, establishing a comprehensive pipeline is of the essence in these cases. Python is a useful tool to enable this aim. Therefore in this paper we aimed to produce a comprehensive pipeline for single cell image analysis using Python. Considering that we use images as our data source the overall pipeline consisted of several tasks. Namely, cellsegmentation, training a cellpose model, measuring the intensity of the protein of interest and other cell components and finally celltracking. The data consisted of images obtained by a high-resolution confocal microscope (90 nm x 90 nm pixels, 1024x1024 image size). The cells that were used were probed with fluorescent markers: one for the protein of interest β-catenin (green) and for the nuclei (red). \

β-catenin is a protein that is involved in cell-cell interactions, it is therefore found in the cell boundaries. However, β-catenin also plays a role in gene regulation, which causes an increase of the protein in the cytoplasm and in the nucleus. This increase can be experimentally induced by using a specific drug that inhibits β-catenin degradation or by inducing the so-called Wnt pathway using Wnt ligands. \

The data consisted of a control dataset, this resembles the "normal" situation without stimulation and a sample dataset which is the situation with stimulation. The aim of this pipeline is to measure the average fluorescence intensity of β-catenin across three different compartements, namely the nucleus, the cytoplasm and the cell boundary. To accomplish this, accurate segmentation of both of the channels was essential. To handle the complex shapes of the cells and the varying intensity contrasts of the cells and nuclei, we used the robust Cellpose. Cellpose is a deeplearning based method that is written in Python. It has a useful API, which also allows for training of custom models based on user data. We used this to train our own segmentation model, to improve the accuracy of segmentation. Using these segmentated masks, we calculated the measurement masks of the different compartements to eventually measure the average fluorescence intensity. 

**#Results**\
**Task 2:** In this task, we have used the cellpose API to perform segmentation by using the pre-trained models (cyto2 and nuclei). This task focused on generating and analyzing outline images and masks (cytoplasm and nuclei) to evaluate the quality of the segmentation.

**Plot**

**Plot description**
-	Laat de outlines en masks zien voor beide channels
-	Zeg iets over de kwaliteit van de segmentation, welke plekken zijn gemist enzo
-	Maybe een gif maar skip dat sorry

**Task 3:** <br /> Next, we had to create a training dataset for the segmentation of the cytoplasm and nuclei by manually correcting the segmentation labels for a subset of images. The goal is to prepare high-quality training data for improving segmentation models. For each dataset (control and sample) we selected 8 images for both channels, in total we manually inspected 32 images. The 8 images were selected by using intervals of 10, this was done to keep the temporal tendencies in the dataset. We did this in ImageJ with the help of the provided macros. The manually corrected images help in improving the accuracy of the segmentation and to better train the model.

**show an example of the manually improved segmentation**
**Explain before and afters**

Task 4: Training the custom cellpose models. <br />
To improve the segmentation accuracy, we trained custom cellpose models for the cytoplasm and the nuclei. This was established with the help of the 32 images that were selected in the previous task.
After training, the training data was segmented using the custom models and compared to the result obtained from the pretrained models. This resulted for the cytoplasm model a more accurate boundary detection and cell shapes and for the nucleus model a better handling of overlapping nuclei.

**show** <br />
The model's training parameters:<br />
Epochs: 

Batch size: 

Learning rate: 


**Task 5.** In this task, the trained models were applied to segment the entire datasets for both channels. With this task we can assess the performance of the model on a larger scale as well as providing visual and dynamic representations of the process.

**show**
  - Images showing the segmentation outlines and masks for both cytoplasm and nucleus.
  - Commentary on the segmentation quality, noting any improvements compared to the initial results.
  - Presentation of GIF animations to provide a comprehensive view of the segmentation performance.
  - Summary of the overall performance and any suggestions for further improvements.


**Task 6: **Measurement masks <br />
To quantify the intensity of the protein of interest in the different compartements, we needed to create measurement masks based on the raw nuclear and cytoplasm masks. We created these masks for the nucleus, cytoplasm and cell boundaries, considering that these are the areas that β-catenin is expressed. The process of making these measurement masks included emoving edge labels, linking cells to their corresponding nuclei, and applying morphological operations such as erosion and dilation. To do this we used the skimage and cv2 libraries. <br />

**show**
example of measurement mask file


**Task 7:** Measuring intensity <br />
Now, the average intensity across different components was ready to be measured. We used the labelled measurement masks generated in the previous step for measuring this. 
For visualization, we plotted the average fluorescence intensity over time for both control and sample conditions, including confidence intervals. This was done to provide a clear comparison of the intensity changes induced by the stimulation. <br />

**show**
show plot that was made in R> handigst om een plot te hebben waarin zowel control als sample zit daaruit kna je conclusies trekken zoals of er meer intensity is in de cellboundary in de control dan in de sample zoiets. 

**Task 8:** <br /> The new version of the Fiji plugin called TrackMate offers a comprehensive suite of tools to perform tracking, data visualization and track analysis in an efficient and user-friendly manner. This versatile tool facilitates the tracking of single cells viewed with fluorescence microscopes, making it an essential tool for biological research  (Tinevez et al., 2017).

Using TrackMate, researchers are able to track the movements and behaviors of individual cells, providing crucial insight into various physiological processes (Fazeli et al., 2020).

**show**
- comments on tracking effort
- animated gifs for the celltracking
  
**Task 9:** <br /> Lastly, in this final task we generated the measurement masks for the compartments with the help of the tracked label mask files which were created in the previous task. The measurements were then done on the tracked data and plots were created of the single cell traces over a period of time.

**Contributions** <br /> During this assignment, all of us find the work distribution to be equal and have each contributed to the report and project to our best abilities

- _init_.py
- get_abs_path.py
- io.py
- create_measurement_masks.py
- measure_intensity.py
- segmentation.py
- training.py

**References/sources** <br /> Fazeli, E., Roy, N. H., Follain, G., Laine, R. F., Von Chamier, L., Hänninen, P. E., Eriksson, J. E., Tinevez, J.-Y., Jacquemet, G., Whitehead, L. W., & Hall, E. (2020). Automated cell tracking using StarDist and TrackMate [version 2; peer review: 3 approved]. https://doi.org/10.12688/f1000research.27019.1

Heumos, L., Schaar, A. C., Lance, C., Litinetskaya, A., Drost, F., Zappia, L., Lücken, M. D., Strobl, D. C., Henao, J., Curion, F., Aliee, H., Ansari, M., Badia-i-Mompel, P., Büttner, M., Dann, E., Dimitrov, D., Dony, L., Frishberg, A., He, D., … Theis, F. J. (2023). Best practices for single-cell analysis across modalities. Nature Reviews Genetics 2023 24:8, 24(8), 550–572. https://doi.org/10.1038/s41576-023-00586-w

Tinevez, J. Y., Perry, N., Schindelin, J., Hoopes, G. M., Reynolds, G. D., Laplantine, E., Bednarek, S. Y., Shorte, S. L., & Eliceiri, K. W. (2017). TrackMate: An open and extensible platform for single-particle tracking. Methods, 115, 80–90. https://doi.org/10.1016/J.YMETH.2016.09.016
