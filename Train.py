import cv2
import numpy as np
import pytesseract
#import NER
#import Perspective_image
import tesseract_OCR
import bbox

filename='Sample.jpeg'
coordinates = 'yolo.txt'
classes = 'classes.txt'
img = cv2.imread(filename)
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
#img = Perspective_image.process_img_scanned(img)
dict = {}
class_list,location = bbox.get_bbox(img,coordinates,classes)     #getting bounding box and respective class
for i in range(0,len(location)):
    dict[class_list[i]]= ''
print(dict)
for i in range(len(location)):
    x,y,w,h = location[i]
    print(img[int(y):int(y + h), int(x):int(x + w)].shape, ' ', x, ' ', w,' ',y,' ',h)
    image, line_conf,sentence= tesseract_OCR.img_data(img[int(y):int(y + h), int(x):int(x + w)])
    dict[class_list[i]] = dict[class_list[i]] +sentence + '\n'
    
print(dict)


