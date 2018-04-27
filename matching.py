import numpy as np
import cv2

img_bgr1 = cv2.imread('img1.jpg')
img_bgr2 = cv2.imread('carplate02.jpg')
img_gray1 = cv2.cvtColor(img_bgr1, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.cvtColor(img_bgr2, cv2.COLOR_BGR2GRAY)
template = cv2.imread('img2.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray1, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.748
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
     cv2.rectangle(img_bgr1, pt, (pt[0]+w, pt[1]+h), (0,255,255),2)
cv2.imshow('detected',img_bgr1)
cv2.waitKey(0)
cv2.DestroyAllWindows()
