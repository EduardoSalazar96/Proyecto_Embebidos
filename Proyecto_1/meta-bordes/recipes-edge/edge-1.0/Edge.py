#import the required libraries
import cv2
import numpy as np

img = cv2.imread('/home/root/myimages/face.jpg')
edges = cv2.Canny(img,100,200)
img = cv2.resize(img,(555,555),interpolation=4)
edges = cv2.resize(edges,(555,555),interpolation=4)
cv2.imshow('Original Image',img)
cv2.imshow('Canny Edges After Contouring', edges) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

#Obtenido de https://docs.opencv.org/master/da/d22/tutorial_py_canny.html
