import cv2
import numpy as np

def get_bbox(image,coordinates,classes):
   bbox = []
   dict_class = {}
   class_list = []
   location  = []

   c = open(classes, 'r')
   cl = c.readlines()
   for i in range(len(cl)):
      dict_class[float(i)] = cl[i].strip()

   f = open(coordinates, 'r')
   data = f.readlines()
   for i in range(len(data)):
      data[i] = data[i].strip()
      data[i] = data[i].split(' ')
      for j in range(0, len(data[i])):
         data[i][j] = float(data[i][j])
      if dict_class[data[i][0]] != 'table':
         _, x, y, w, h = data[i]
         x= x*image.shape[1]
         w=w*image.shape[1]
         x = x - w/2
         h= h*image.shape[0]
         y=y*image.shape[0]
         y = y - h/2
         location.append([x,y,w,h])
         class_list.append(dict_class[data[i][0]])
   f.close()
   c.close()

   return class_list,location # will return bbox image in form of array, just need to cv2.imshow




if __name__ == '__main__':
   coordinates = 'yolo.txt'
   classes = 'classes.txt'
   image = cv2.imread('Sample.jpeg')
   bbox = []
   dict_class = {}

   c = open(classes, 'r')
   cl = c.readlines()
   for i in range(len(cl)):
      dict_class[float(i)] = cl[i].strip()

   f = open(coordinates, 'r')
   data = f.readlines()
   for i in range(len(data)):
      data[i] = data[i].strip()
      data[i] = data[i].split(' ')
      for j in range(0, len(data[i])):
         data[i][j] = float(data[i][j])
      if dict_class[data[i][0]] != 'table':
         _, x, y, w, h = data[i]
         x = x * image.shape[0]
         w = w * image.shape[0]
         x = x - w / 2
         h = h * image.shape[1]
         y = y * image.shape[1]
         y = y - h / 2
         bbox.append(bbox, image[int(y):int(y + h), int(x):int(x + w)])

   f.close()
   c.close()





