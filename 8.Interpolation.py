#Interpolation
# import library
import mahotas as mh
import numpy as np
from pylab import imshow, show
#buat boolean untuk keadaan aray 8,8 keadaan bool false
regions = np.zeros((8,8), bool)
#Mengatur wilayah 3x3 di bagian kiri atas menjadi True, dan  2x2 di bagian kanan bawah menjadi True
regions[:3,:3] =1 
regions[6:,6:]= 1
# Melabeli wilayah yang terhubung pada array
labeled, nr_objects = mh.label(regions)
# tampilkan
imshow(labeled, interpolation='nearest')
labeled, nr_objects = mh.label(regions, np.ones((3, 3), bool))
sizes = mh.labeled.labeled_size(labeled)
print('Background size:', sizes[0])
print('Size of first region:', sizes[1])
array = np.random.random_sample(regions.shape)
sums = mh.labeled_sum(array, labeled)
print('Sum of first region:', sums[1])
show()