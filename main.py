import os
from scripts.segmentation import segment_images
from scripts.create_measurement_masks import create_measurement_masks
from scripts.measure_intensity import measure_intensity


def main():
    # Directories
    data_dir = 'data'
    out_dir = 'output'

    control_cyt_data_dir = os.path.join(data_dir, 'cyt', 'control')
    control_nuc_data_dir = os.path.join(data_dir, 'nuc', 'control')

    sample_cyt_data_dir = os.path.join(data_dir, 'cyt', 'sample')
    sample_nuc_data_dir = os.path.join(data_dir, 'nuc', 'sample')

    train_cyt_data_dir = os.path.join(data_dir, 'cyt', 'train')
    train_nuc_data_dir = os.path.join(data_dir, 'nuc', 'train')

    segmentation_cyt_control_dir = os.path.join(out_dir, 'segmentation', 'cyt', 'control')
    segmentation_nuc_control_dir = os.path.join(out_dir, 'segmentation', 'nuc', 'control')

    segmentation_cyt_sample_dir = os.path.join(out_dir, 'segmentation', 'cyt', 'sample')
    segmentation_nuc_sample_dir = os.path.join(out_dir, 'segmentation', 'nuc', 'sample')

    # training_cyt_output_dir = os.path.join(out_dir, 'training', 'cyt', 'custom_model')
    # training_nuc_output_dir = os.path.join(out_dir, 'training', 'nuc', 'custom_model')

    masks_cyt_control_dir = os.path.join(out_dir, 'masks', 'cyt', 'control')
    masks_nuc_control_dir = os.path.join(out_dir, 'masks', 'nuc', 'control')

    masks_cyt_sample_dir = os.path.join(out_dir, 'masks', 'cyt', 'sample')
    masks_nuc_sample_dir = os.path.join(out_dir, 'masks', 'nuc', 'sample')

    intensity_cyt_control_csv = os.path.join(out_dir, 'intensity', 'cyt', 'control_intensity_cyt.csv')
    intensity_nuc_control_csv = os.path.join(out_dir, 'intensity', 'nuc', 'control_intensity_nuc.csv')

    intensity_cyt_sample_csv = os.path.join(out_dir, 'intensity', 'cyt', 'sample_intensity_cyt.csv')
    intensity_nuc_sample_csv = os.path.join(out_dir, 'intensity', 'nuc', 'sample_intensity_nuc.csv')

    # Step 1: Segment images
    print("Segmenting control images...")
    print("Cytoplasm.....:")
    segment_images(control_cyt_data_dir, segmentation_cyt_control_dir, "cyt")
    print("Nucleus......:")
    segment_images(control_nuc_data_dir, segmentation_control_dir, "nuc")

    print("Segmenting sample images...")
    print("Cytoplasm.....:")
    segment_images(sample_cyt_data_dir, segmentation_cyt_sample_dir, "cyt")
    print("Nucleus......:")
    segment_images(sample_nuc_data_dir, segmentation_sample_dir, "nuc")


    # Step 2: Train custom model (optional, based on assignment description)
    # Uncomment the following lines if training a custom model is needed
    # print("Training custom model...")
    # print("Cytoplasm.....:")
    # train_custom_model(train_cyt_data_dir, training_output_dir)
    # print("Nucleus......:")
    # train_custom_model(train_nuc_data_dir, training_output_dir)


    # Step 3: Create measurement masks
    print("Creating measurement masks for control images...")
    print("Cytoplasm.....:")
    create_measurement_masks(segmentation_cyt_control_dir, masks_cyt_control_dir)
    print("Nucleus......:")

    print("Creating measurement masks for sample images...")
    print("Cytoplasm.....:")
    create_measurement_masks(segmentation_cyt_sample_dir, masks_cyt_sample_dir)
    print("Nucleus......:")

    # Step 4: Measure intensity
    print("Measuring intensity for control images...")
    print("Cytoplasm.....:")
    measure_intensity(masks_cyt_control_dir, control_cyt_data_dir, intensity_cyt_control_csv)
    print("Nucleus......:")

    print("Measuring intensity for sample images...")
    print("Cytoplasm.....:")
    measure_intensity(masks_cyt_sample_dir, sample_cyt_data_dir, intensity_cyt_sample_csv)
    print("Nucleus......:")


    print("Analysis pipeline completed successfully!")


if __name__ == '__main__':
    main()
