import cv2
import numpy as np

filename='/Users/pushkarsingh/Downloads/16rgb.png'
img=cv2.imread(filename)
print('Height if image: ',len(img))
print('Width of image: ',len(img[0]))
pixel_data=[]
for i in range(len(img)):
    for j in range(len(img[0])):
        pixel_data.append(img[i][j])
        
print('Total number of pixels: ',len(pixel_data))

words=set()

for word in pixel_data:
    words.add(str(word))
    
print('Total number of different colors: ',len(words)-1)
