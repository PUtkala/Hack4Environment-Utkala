import json
import numpy as np
from types import SimpleNamespace
from records import Record
import sklearn.cluster as sklearn
from matplotlib import pyplot as plt


dist = 50
limit = 100

color_list = ("b.", "r.", "g.", "m.", "c.", "y.")

with open('jsondata.json') as f:
	x = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

print(x.features[2].properties.filename)
X = np.zeros((1, 2))
list_rec=[]
weight_list = []

for i in range(len(x.features)):
    list_rec.append(Record(i, x.features[i].properties))
    X = np.vstack((X, [list_rec[i].lat, list_rec[i].lon]))
    list_rec[i].calc_weight()
    weight_list.append(list_rec[i].weight) 


X = X[1:-1]
weight_list = weight_list[0:-1]

#print(np.unique(cat_list,return_index=True))
#print(x.features[6].properties)

cluster = sklearn.DBSCAN(eps=0.0001, min_samples=100).fit(X,y=None,sample_weight=weight_list)

dumps = []
cluster_count = np.unique(cluster.labels_)
idx = 0
while idx < max(cluster_count):
    dumps.append(list_rec[np.where(cluster.labels_==idx)[0][0]])
    idx+=1

final_dict = {}
for i in dumps:
    final_dict.update({i.photo_id:{"lat":i.lat,"lon":i.lon,"filename":i.filename}})

print(final_dict)
with open("dumps.json", 'w') as w:
    json.dump(final_dict,w)

#print(cluster_count)
# for i in range(len(list_rec)-1):
#     if cluster.labels_[i] != -1:
#         list_rec[i].color = color_list[cluster.labels_[i]%6]
#     plt.plot(X[i,1],X[i,0], list_rec[i].color)
#     plt.grid("on")

# plt.show()

