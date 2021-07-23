import json
import Train
invoice_dict,tables = Train.Train('Sample.jpeg','yolo.txt')
with open('data.json', 'w') as fp:
    json.dump(invoice_dict, fp)
print(tables)