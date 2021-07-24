import cv2
import tesseract_OCR
import bbox
import Table_extract
import Searchable_pdf_converter



def Train(filename='Sample.jpeg',coordinates = 'yolo.txt',classes = 'classes.txt',dict={}):
    img = cv2.imread(filename)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print(img.shape)
    class_list,location = bbox.get_bbox(img,coordinates,classes)     #getting bounding box and respective class
    tables = []
    for i in range(0,len(location)):
        dict[class_list[i]]= ''
    j=0
    for i in range(len(location)):
        x,y,w,h = location[i]
        print(class_list[i],' ',img[int(y):int(y + h), int(x):int(x + w)].shape, ' ', x, ' ', w,' ',y,' ',h)
        if class_list[i] == 'table':
            table_img = img[int(y):int(y + h), int(x):int(x + w)]
            j = j+1
            print(x,' ',y)
            cv2.imwrite('table.jpg',table_img)
            Searchable_pdf_converter.img_to_searchablepdf('table.jpg')
            table_df=Table_extract.table_extract('test.pdf')
            Table_extract.save_table(table_df,table_num=j)
            Table = table_df
            table = Table.to_dict('split')
            del table['index']
            del table['columns']
            tables['table'+str(j)] = table
            dict[class_list[i]] = tables
        else:
            image, line_conf,sentence= tesseract_OCR.img_data(img[int(y):int(y + h), int(x):int(x + w)])
            dict[class_list[i]] = dict[class_list[i]] +sentence + '\n'
    print(dict)
    return dict


