import os
from cellpose import models, io

from scripts.utils.io import load_images
from scripts.utils.get_abs_path import get_file, get_lst_path


import numpy as np
import matplotlib.pyplot as plt

from skimage import morphology, io as skimage_io


# Function to perform segmentation
def segment_images(input_folder, output_folder, cell_component):
    channels = [0, 0]
    diam = None

    if cell_component == "cyt":
        model = models.Cellpose(gpu=False, model_type='cyto2')
        channels = [2, 0]
        # diam = 100
    elif cell_component == "nuc":
        model = models.Cellpose(gpu=False, model_type='nuclei')
        channels = [1, 2]
        diam = 80
    else:
        raise ValueError("Invalid cell component, use 'cyt' for cytoplasm and 'nuc' for nucleus")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("state files variable")
    files = os.listdir(input_folder)
    images = load_images(input_folder)

    for img, file in zip(images, files):
        print("model eval")
        masks, flows, styles, diams = model.eval(img, diameter=diam, channels=channels)

        # error fix instead of numpy.float64
        diams = str(diams)

        print("masks to seg")
        # out_file = output_folder + f"/{cell_component}_" + str(file.replace('.tif', ''))
        out_file = output_folder + "/" + str(file.replace('.tif', ''))
        print(out_file)
        io.masks_flows_to_seg(img, masks, flows, out_file, diams)

        # Save masks to file
        # mask_save_path = mask_folder + f"/{cell_component}_" + str(file.replace('.tif', '_mask.tif'))
        mask_save_path = output_folder + "/" + str(file.replace('.tif', '_mask.tif'))
        io.imsave(mask_save_path, masks.astype(np.uint16))
        print(f"Saved masks to: {mask_save_path}")

        # Generate and save outlines
        # Create a binary mask for the outlines
        outlines = np.zeros_like(masks, dtype=bool)
        for unique_value in np.unique(masks):
            if unique_value == 0:  # Skip background
                continue
            mask = masks == unique_value
            outline = morphology.dilation(mask) ^ mask
            outlines |= outline

        # Convert boolean outlines to a format suitable for saving
        outlines_image = outlines.astype(np.uint16) * 65535  # Max value for uint16 to ensure visibility
        outline_save_path = output_folder + "/" + str(file.replace('.tif', '_outline.tif'))
        skimage_io.imsave(outline_save_path, outlines_image)

        print(f"Saved outlines to: {outline_save_path}")

        # Optional: visualize the original image and the masks
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].imshow(img, cmap='gray')
        ax[0].set_title('Original Image')
        ax[1].imshow(masks, cmap='jet')
        ax[1].set_title('Segmented Masks')
        plt.show()

