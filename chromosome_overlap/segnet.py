import numpy as np
import h5py

def prep_data(image_set):
    train_data = []
    train_label = []
    # for every image
    for i in range(0,len(image_set)):
        grey = image_set[i,:,:,0]
        mask = image_set[i,:,:,1]
        train_data.append(grey)
        train_label.append(mask)
    return np.array(train_data), np.array(train_label)

h5f = h5py.File('overlapping_chromosomes_examples.h5','r')
image_set = h5f['dataset_1'][:]
train_data, train_label = prep_data(image_set)
print train_data.shape
print train_label.shape
