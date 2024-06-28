from scripts.segmentation import segment_images
from scripts.create_measurement_masks import create_measurement_masks
import os
from scripts.measure_intensity import measure_intensity
import time

start = time.perf_counter()
segment_images('data/raw_data/control/cyt', 'output/segmentations/control/cyt', "cyt")
lap1 = time.perf_counter()
print(f'Time taken: {lap1-start:.6f} seconds')
print(f'Total time taken: {lap1-start:.6f} seconds')

segment_images('data/raw_data/sample/cyt', 'output/segmentations/sample/cyt',  "cyt")
lap2 = time.perf_counter()
print(f'Time taken: {lap2-lap1:.6f} seconds')
print(f'Total time taken: {lap2-start:.6f} seconds')

segment_images('data/raw_data/control/nuc', 'output/segmentations/control/nuc', "nuc")
lap3 = time.perf_counter()
print(f'Time taken: {lap3-lap2:.6f} seconds')
print(f'Total time taken: {lap3-start:.6f} seconds')

segment_images('data/raw_data/sample/nuc', 'output/segmentations/sample/nuc',  "nuc")
end = time.perf_counter()
print(f'Time taken: {end-lap3:.6f} seconds')
print(f'Total time taken: {end-start:.6f} seconds')

# # control
# lst_cell_mask = ['temp_output/control/cyt/segmentation/' + elem for elem in os.listdir('temp_output/control/cyt/segmentation') if "_mask" in elem]
# lst_nuc_mask = ['temp_output/control/nuc/segmentation/' + elem for elem in os.listdir('temp_output/control/nuc/segmentation') if "_mask" in elem]
#
#
# for cell_mask, nuc_mask in zip(lst_cell_mask, lst_nuc_mask):
#     out = 'temp_output/measure_mask/control'
#     create_measurement_masks(cell_mask, nuc_mask, out)
#
# # sample
# lst_cell_mask = ['temp_output/sample/cyt/segmentation/' + elem for elem in os.listdir('temp_output/sample/cyt/segmentation') if "_mask" in elem]
# lst_nuc_mask = ['temp_output/sample/nuc/segmentation/' + elem for elem in os.listdir('temp_output/sample/nuc/segmentation') if "_mask" in elem]
#
# for cell_mask, nuc_mask in zip(lst_cell_mask, lst_nuc_mask):
#     out = 'temp_output/measure_mask/sample'
#     create_measurement_masks(cell_mask, nuc_mask, out)

# measure_intensity('results/masks/control', 'data/control', 'results/intensity/control_intensity.csv')
# measure_intensity('results/masks/sample', 'data/sample', 'results/intensity/sample_intensity.csv')