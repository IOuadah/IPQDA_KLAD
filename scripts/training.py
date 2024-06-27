from cellpose import models, io
import os

#use io.py here somewhere en we moeten de training data nog maken

# Function to train custom Cellpose model
def train_custom_model(train_folder, model_output):
    model = models.CellposeModel(gpu=False, pretrained_model='cyto3')
    images = io.imread_train(train_folder)
    labels = io.imread_train_labels(train_folder)
    model.train(images, labels, train_folder, save_path=model_output)

# Train custom model on manually corrected images
# train_custom_model('data/train', 'results/training/custom_model')
