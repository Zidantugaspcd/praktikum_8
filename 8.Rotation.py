#Rotation
# import library
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt
# import foto dari file path dari penyimpanan
mrbean = cv.imread("D:\SEMESTER 6\Pengolahan Citra Digital\mrbean\Bean.jpg")
# inisialisaasi nilai tinggi dan lebar mrbean dengan h dan w
h, w = mrbean.shape[:2]
#rotasikan mrbean sebesar -180 derajat dengan faktor skala 0.5
rotation_matrix = cv.getRotationMatrix2D((w/2,h/2), -180, 0.5)
# terapkan transformasi affine pada citra menggunakan matriks transformasi rotasi 
rotated_mrbean = cv.warpAffine(mrbean,rotation_matrix, (w, h))
# tampilkan gambar dan convert dari BGR ke RGB
plt.imshow(cv.cvtColor(rotated_mrbean,cv.COLOR_BGR2RGB))
plt.title("Rotation") 
plt.show()