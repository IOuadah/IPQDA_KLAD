from scripts.segmentation import segment_images
from scripts.create_measurement_masks import create_measurement_masks
segment_images('data/cyt/control', 'temp_output/segmentation/control', "cyt")
segment_images('data/cyt/sample', 'temp_output/segmentation/sample', "cyt")
segment_images('data/cyt/control', 'temp_output/segmentation/control', "cyt")
segment_images('data/nuc/control', 'temp_output/segmentation/control', "nuc")

# create_measurement_masks()