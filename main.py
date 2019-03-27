import cv2

filename='FILEPATH-TO-IMAGE'
img=cv2.imread(filename)
print('Height if image: ',len(img))
print('Width of image: ',len(img[0]))
pixel_data=[]
for i in range(len(img)):
    for j in range(len(img[0])):
        pixel_data.append(img[i][j])
        
print('Total number of pixels: ',len(pixel_data))

colors=set()

for color in pixel_data:
    colors.add(str(color))
    
print('Total number of different colors: ',len(colors)-1)
