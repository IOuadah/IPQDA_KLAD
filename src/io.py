from cellpose import io

from src import time_files

io.logger_setup()

channels = [0, 0]
lst_img = []

for filename in time_files:
    if "G" in filename:
        channels = [2, 0]  # = [cytoplasm, nucleus] [G, non-existent]
    elif "R" in filename:
        channels = [2, 1]  # = [cytoplasm, nucleus] [G, R]
    img = io.imread(filename)

    lst_img.append(img)

# how do we save the ndarrays so we dont need to run it all the time
