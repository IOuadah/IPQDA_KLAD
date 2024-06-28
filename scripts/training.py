from cellpose import models, io
import os

#use io.py here somewhere en we moeten de training data nog maken

# Function to train custom Cellpose model
def train_custom_model(train_folder, model_output, cell_component):
    if cell_component == "cyt":
        model = models.CellposeModel(gpu=False, pretrained_model='cyto2')
    elif cell_component == "nuc":
        model = models.CellposeModel(gpu=False, pretrained_model='nuclei')

    images = io.imread_train(train_folder)
    labels = io.imread_train_labels(train_folder)
    model.train(images, labels, train_folder, save_path=model_output)


from cellpose import io, models, train
io.logger_setup()

output = io.load_train_test_data(train_dir, image_filter="_img", mask_filter="_seg.npy", look_one_level_down=False)
images, labels, image_names = output

# e.g. retrain a Cellpose model
model = models.CellposeModel(model_type="cyto3")

model_path = train.train_seg(model.net, train_data=images, train_labels=labels,
                            channels=[1,2], normalize=True,
                            weight_decay=1e-4, SGD=True, learning_rate=0.1,
                            n_epochs=100, model_name="my_new_model")

# Train custom model on manually corrected images
# train_custom_model('data/train', 'results/training/custom_model')
