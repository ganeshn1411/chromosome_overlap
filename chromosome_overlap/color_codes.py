import h5py
from matplotlib import pyplot as plt
import PIL as pillow
from PIL import Image
import numpy

yellow = [255,229,0]
red = [127,0,0]
light_blue = [0,212,255]
dark_blue = [0,0,127]

color_names = ['yellow','red','light_blue','dark_blue']
rgb_vlaues = [[255,229,0],[127,0,0],[0,212,255],[0,0,127]]

my_val = [255,229,0] 
if my_val in rgb_vlaues:
    print color_names[rgb_vlaues.index(my_val)]

h5f = h5py.File('overlapping_chromosomes_examples.h5','r')
pairs = h5f['dataset_1'][:]

print pairs.shape


h5f.close()

grey = pairs[220,:,:,0]
mask = pairs[220,:,:,1]
#print mask
#print pairs[220,0,0,1]
#pix = mask.reshape(190,189,3)
#print pix[0][1]

#image_size = [10,10]
#print mask
#for x in range(1,image_size[0]):
#    for y in range(1,image_size[1]):
#        print mask[x,y]

for pixel in grey:
    print pixel
#%matplotlib inline
plt.subplot(121)
plt.imshow(grey)
plt.title('max='+str(grey.max()))
plt.subplot(122)
plt.imshow(mask)
plt.show()

plt.imshow(numpy.random.rand(5,4))
print numpy.random.rand(5,4)
print numpy.random.rand(5,4).shape
plt.show()

#import matplotlib.image as mpimage
#print mpimage.imread(mask)
