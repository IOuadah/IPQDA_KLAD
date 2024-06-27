import os
from cellpose import models, io

from scripts.utils.io import load_images
from scripts.utils.get_abs_path import get_file, get_lst_path


import numpy as np
import matplotlib.pyplot as plt


# Function to perform segmentation
def segment_images(input_folder, output_folder, cell_component):
    # Load the Cellpose model
    model = models.Cellpose(gpu=False, model_type='cyto2')

    channels = [0, 0]
    if cell_component == "cyt":
        channels = [2, 0]  # = [cytoplasm, nucleus] [G, non-existent]
    elif cell_component == "nuc":
        model = models.Cellpose(gpu=False, model_type='nuclei')
        channels = [2, 1]  # = [cytoplasm, nucleus] [G, R]
    else:
        raise ValueError("Invalid cell component, use 'cyt' for cytoplasm and 'nuc' for nucleus")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("state files variable")
    files = os.listdir(input_folder)
    # print(files, type(files))
    images = load_images(input_folder)

    for img in images:
        plt.imshow(img)
        plt.axis('off')
        plt.show()

    for img, file in zip(images, files):
        print("model eval")
        masks, flows, styles, diams = model.eval(img, diameter=None, channels=channels)

        # error fix instead of numpy.float64
        diams = str(diams)

        print("masks to seg")
        out_file = output_folder + "/" + str(file.replace('.tif', ''))
        print(out_file)
        # io.masks_flows_to_seg(img, masks, flows, out_file, diams)
        io.save_masks(img, masks, flows, out_file)


# out_path = os.path.join('temp_output', "segmentation", "control")


# Segment control and sample datasets
# segment_images('data/cyt/control', 'temp_output/segmentation/control', "cyt")
# segment_images('data/nuc/control', 'temp_output/segmentation/control', "nuc")
# segment_images('data/cyt/sample', 'temp_output/segmentation/sample', "cyt")
