import os
import cv2
import numpy as np
from cellpose.io import imread, imsave
from skimage.morphology import dilation, erosion, disk
# from skimage.io import imread, imsave


def create_measurement_masks(cell_mask_path, nucleus_mask_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    cell_mask = imread(cell_mask_path)
    nucleus_mask = imread(nucleus_mask_path)
    # Initialize blank masks
    height, width = nucleus_mask.shape
    nucleus_total_mask = np.zeros((height, width), dtype=np.uint8)
    cytoplasm_total_mask = np.zeros((height, width), dtype=np.uint8)
    boundary_total_mask = np.zeros((height, width), dtype=np.uint8)
    # Link cells and nuclei
    linked_mask = cell_mask.copy()
    for region in np.unique(nucleus_mask):
        if region == 0:
            continue
        cell_region = np.unique(cell_mask[nucleus_mask == region])
        if len(cell_region) == 1:
            linked_mask[cell_mask == cell_region[0]] = region
    # Create measurement masks
    dilated_mask = dilation(linked_mask, disk(3))
    eroded_mask = erosion(linked_mask, disk(3))
    cell_boundary = dilated_mask - eroded_mask
    cytoplasm_mask = linked_mask - nucleus_mask
    for region in np.unique(linked_mask):
        if region == 0:
            continue
        nucleus_total_mask[nucleus_mask == region] = region
        cytoplasm_total_mask[cytoplasm_mask == region] = region
        boundary_total_mask[cell_boundary == region] = region
    # Save the combined masks
    imsave(os.path.join(output_path, 'nucleus_mask.png'), nucleus_total_mask)
    imsave(os.path.join(output_path, 'cytoplasm_mask.png'), cytoplasm_total_mask)
    imsave(os.path.join(output_path, 'boundary_mask.png'), boundary_total_mask)

# def create_measurement_masks(cell_mask_path, nucleus_mask_path, output_path):
#     if not os.path.exists(output_path):
#         os.makedirs(output_path)
#     cell_mask = imread(cell_mask_path)
#     nucleus_mask = imread(nucleus_mask_path)
#     # Link cells and nuclei
#     linked_mask = cell_mask.copy()
#     for region in np.unique(nucleus_mask):
#         if region == 0:
#             continue
#         cell_region = np.unique(cell_mask[nucleus_mask == region])
#         if len(cell_region) == 1:
#             linked_mask[cell_mask == cell_region[0]] = region
#     # Create measurement masks
#     cell_boundary = dilation(linked_mask, disk(3)) - linked_mask
#     cytoplasm_mask = linked_mask - nucleus_mask
#     for region in np.unique(linked_mask):
#         if region == 0:
#             continue
#         nuc = nucleus_mask == region
#         cyt = cytoplasm_mask == region
#         bound = cell_boundary == region
#         imsave(os.path.join(output_path, f'nucleus_{region}.png'), nuc.astype(np.uint8))
#         imsave(os.path.join(output_path, f'cytoplasm_{region}.png'), cyt.astype(np.uint8))
#         imsave(os.path.join(output_path, f'boundary_{region}.png'), bound.astype(np.uint8))


# Create measurement masks for control and sample datasets
# create_measurement_masks('results/segmentation/control', 'results/masks/control')
# create_measurement_masks('results/segmentation/sample', 'results/masks/sample')
