from cellpose import models
import os

# Function to train custom Cellpose model
def train_custom_model(train_folder, model_output):
    model = models.CellposeModel(gpu=True, pretrained_model='cyto2')
    images = io.imread_train(train_folder)
    labels = io.imread_train_labels(train_folder)
    model.train(images, labels, train_folder, save_path=model_output)

# Train custom model on manually corrected images
train_custom_model('data/train', 'results/training/custom_model')
