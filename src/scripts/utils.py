import os
from skimage.io import imread, imsave

def load_images(folder):
    images = []
    files = sorted(os.listdir(folder))
    for file in files:
        if file.endswith('.tif'):
            img = imread(os.path.join(folder, file))
            images.append(img)
    return images

def save_image(image, path):
    imsave(path, image)
