#Translation
# import library
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
# import foto dari file path
mrbean=cv.imread("D:\SEMESTER 6\Pengolahan Citra Digital\image\Bean.jpg")
# inisialisaasi nilai tinggi dan lebar image dengan h dan w
h,w = mrbean.shape [:2]
#Translasi dilakukan relatif terhadap ukuran citra, dengan translasi tinggi setengah dari tinggi citra dan translasi lebar setengah dari lebar citra
half_height, half_width = h//4, w//8
#Menentukan matriks transformas
transition_matrix = np.float32([[1, 0,half_width],[0, 1,half_height]])
#Melakukan transformasi affine pada citra
img_transition = cv.warpAffine(mrbean, transition_matrix, (w, h))
# tampilkan gambar dengan mengubah dari BGR ke RGB
plt.imshow(cv.cvtColor(img_transition,cv.COLOR_BGR2RGB))
plt.title("Translation") 
plt.show()