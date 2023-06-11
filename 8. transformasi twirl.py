# Transformasi Twirl
# import library
import matplotlib.pyplot as plt
import cv2 as cv
from skimage.transform import swirl
# panggil dan baca file untuk di buka di python
loop=plt.imread('D:\SEMESTER 6\Pengolahan Citra Digital\image\habibi.jpg')
# buat imgae loop menjadi swirled dengan atribut sebagai berikut:
swirledloop = swirl(loop, rotation=0, strength=10, radius=120)
# buat figur subllot untuk 2 plot dan dihilangkan sumbu
fig,(ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8,3), sharex=True, sharey=True)
# tampilkan masing masing gambar
ax0.imshow(loop, cmap=plt.cm.gray)
ax0.axis('off')
ax1.imshow(swirledloop, cmap=plt.cm.gray)
ax1.axis('off')
plt.show()