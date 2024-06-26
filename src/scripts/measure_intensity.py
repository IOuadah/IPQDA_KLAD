import os
import pandas as pd
from skimage.io import imread
from skimage.measure import regionprops_table

def measure_intensity(mask_folder, image_folder, output_csv):
    data = []
    for file in os.listdir(mask_folder):
        if file.endswith('.png'):
            region = file.split('_')[1].replace('.png', '')
            mask = imread(os.path.join(mask_folder, file))
            image = imread(os.path.join(image_folder, f'{region}.tif'))
            props = regionprops_table(mask, image, properties=['label', 'mean_intensity'])
            df = pd.DataFrame(props)
            df['region'] = region
            data.append(df)
    result = pd.concat(data)
    result.to_csv(output_csv, index=False)

# Measure intensity for control and sample datasets
measure_intensity('results/masks/control', 'data/control', 'results/intensity/control_intensity.csv')
measure_intensity('results/masks/sample', 'data/sample', 'results/intensity/sample_intensity.csv')
