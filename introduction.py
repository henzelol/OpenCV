import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('carplate.jpeg',cv2.IMREAD_GRAYSCALE)

#IMREAD_COLOR = -1
#IMREAD_UNCHANGED = -1

cv2.imshow('car plate', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.plot([50,100],[80,100], 'c', linewidth=5)
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.show()

cv2.imwrite('testing.jpeg', img)
