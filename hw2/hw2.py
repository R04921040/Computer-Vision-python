import numpy as np
import cv2
import matplotlib.pyplot as plt 

lena = cv2.imread('lena.bmp')

#print(lena)
#print(lena.shape)

height , length , channels = lena.shape

histogram = np.zeros(256)

T = 128
thresholding = np.zeros([512,512])
for i in range(height):
    for j in range(length):
        if lena[i , j , 0] >= T:
            thresholding[i , j] = 255

        histogram[lena[i , j , 0]] += 1


#cv2.imwrite('thresholding.bmp', thresholding)
#plt.bar(range(256) , histogram , 1)
#plt.show()