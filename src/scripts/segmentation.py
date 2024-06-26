import os
from cellpose import models, io
import numpy as np
import matplotlib.pyplot as plt

# Load the Cellpose model
model = models.Cellpose(gpu=True, model_type='cyto2')

# Function to perform segmentation
def segment_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    files = os.listdir(input_folder)
    for file in files:
        img = io.imread(os.path.join(input_folder, file))
        masks, flows, styles, diams = model.eval(img, diameter=None, channels=[0,0])
        io.masks_flows_to_seg(img, masks, flows, diams, os.path.join(output_folder, file.replace('.tif', '')))

# Segment control and sample datasets
# segment_images('data/control', 'results/segmentation/control')
# segment_images('data/sample', 'results/segmentation/sample')
