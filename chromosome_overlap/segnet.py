import numpy as np
import h5py

def prep_data(image_set):
    train_data = []
    train_label = []
    # for every image
    for i in range(0,len(image_set)):
        # input image
        grey = image_set[i,:,:,0]
        # output image
        mask = image_set[i,:,:,1]
        # add input image 
        train_data.append(grey)
        # add output image with binarized columns
        train_label.append(binarylab(mask))
    return np.array(train_data), np.array(train_label)

# function that will convert output label into binarized labels
def binarylab(labels):
    # 190 * 189 is size of each image, each image has 4 classes
    x = np.zeros([190,189,4])    
    for i in range(190):
        for j in range(189):
            x[i,j,labels[i][j]]=1
    return x

h5f = h5py.File('overlapping_chromosomes_examples.h5','r')
image_set = h5f['dataset_1'][:]
train_data, train_label = prep_data(image_set)
print train_data.shape
print train_label.shape
