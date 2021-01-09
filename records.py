import numpy as np
import re
import json

class Record():
    def __init__(self, index, properties):
        self.index = index
        self.datetime = properties.datetime
        self.filename = properties.filename
        self.lat = properties.lat
        self.lon = properties.lon
        self.model = properties.model
        self.photo_id = properties.photo_id
        self.result_string = properties.result_string
        self.color="k."
        self.weight = 0

    def calc_weight(self):
        #re.sub("..*$", "",self.result_string)
        temp = self.result_string.split(',')
        temp2 = []
        category = []
        temp3 =[]
        detail=[]
        value=[]
        for i in range(len(temp)-1):
            temp2.append(temp[i].split('.'))    
        for i in temp2:
            category.append(i[0::2])
            temp3.append(i[1::2])
        temp3=np.asarray_chkfinite(temp3)    
        for i in range(temp3.shape[0]):
            for j in range(temp3.shape[1]):
                detail.append(temp3[i,j].split()[0])
                value.append(temp3[i,j].split()[1])
        flat_list = []
        for sublist in category:
            for item in sublist:
                flat_list.append(item)     
        for i in range(len(flat_list)):
            if flat_list[i] == 'alcohol':
                self.weight += int(value[i]) * 5
            elif flat_list[i] == 'brands':
                self.weight += int(value[i]) * 1
            elif flat_list[i] == 'coastal':
                self.weight += int(value[i]) * 8
            elif flat_list[i] == 'coffee':
                self.weight += int(value[i]) * 1
            elif flat_list[i] == 'dumping':
                self.weight += int(value[i]) * 10
            elif flat_list[i] == 'food':
                self.weight += int(value[i]) * 2
            elif flat_list[i] == 'industrial':
                self.weight += int(value[i]) * 8
            elif flat_list[i] == 'other':
                self.weight += int(value[i]) * 2
            elif flat_list[i] == 'sanitary':
                self.weight += int(value[i]) * 3
            elif flat_list[i] == 'smoking':
                self.weight += int(value[i]) * 2
            elif flat_list[i] == 'softdrinks':
                self.weight += int(value[i]) * 5    
            else:
                self.weight += 0   

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)                                         
        

