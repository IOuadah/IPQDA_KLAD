import os
from scripts.segmentation import segment_images
from scripts.training import train_custom_model
from scripts.create_measurement_masks import create_measurement_masks
from scripts.measure_intensity import measure_intensity


def main():
    # Directories
    data_dir = 'data'
    results_dir = 'results'

    control_data_dir = os.path.join(data_dir, 'control')
    sample_data_dir = os.path.join(data_dir, 'sample')
    train_data_dir = os.path.join(data_dir, 'train')

    segmentation_control_dir = os.path.join(results_dir, 'segmentation', 'control')
    segmentation_sample_dir = os.path.join(results_dir, 'segmentation', 'sample')

    training_output_dir = os.path.join(results_dir, 'training', 'custom_model')

    masks_control_dir = os.path.join(results_dir, 'masks', 'control')
    masks_sample_dir = os.path.join(results_dir, 'masks', 'sample')

    intensity_control_csv = os.path.join(results_dir, 'intensity', 'control_intensity.csv')
    intensity_sample_csv = os.path.join(results_dir, 'intensity', 'sample_intensity.csv')

    # Step 1: Segment images
    print("Segmenting control images...")
    segment_images(control_data_dir, segmentation_control_dir)

    print("Segmenting sample images...")
    segment_images(sample_data_dir, segmentation_sample_dir)

    # Step 2: Train custom model (optional, based on assignment description)
    # Uncomment the following lines if training a custom model is needed
    # print("Training custom model...")
    # train_custom_model(train_data_dir, training_output_dir)

    # Step 3: Create measurement masks
    print("Creating measurement masks for control images...")
    create_measurement_masks(segmentation_control_dir, masks_control_dir)

    print("Creating measurement masks for sample images...")
    create_measurement_masks(segmentation_sample_dir, masks_sample_dir)

    # Step 4: Measure intensity
    print("Measuring intensity for control images...")
    measure_intensity(masks_control_dir, control_data_dir, intensity_control_csv)

    print("Measuring intensity for sample images...")
    measure_intensity(masks_sample_dir, sample_data_dir, intensity_sample_csv)

    print("Analysis pipeline completed successfully!")


if __name__ == '__main__':
    main()
