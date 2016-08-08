import h5py
from matplotlib import pyplot as plt

h5f = h5py.File('overlapping_chromosomes_examples.h5','r')
pairs = h5f['dataset_1'][:]
h5f.close()

for i in range(1,50):
    print i
    grey = pairs[i,:,:,0]
    mask = pairs[i,:,:,1]
    #%matplotlib inline
    plt.subplot(121)
    plt.imshow(grey)
    plt.title('max='+str(grey.max()))
    plt.subplot(122)
    plt.imshow(mask)
    plt.show()