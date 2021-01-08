import json
import numpy as np
from types import SimpleNamespace
from records import Record
import sklearn.cluster as sklearn


dist = 50
limit = 100

with open('jsondata.json') as f:
	x = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

print(x.features[2].properties.filename)
X = np.zeros((1, 2))
list_rec=[]

for i in range(100):
    list_rec.append(Record(i, x.features[i].properties))
    X = np.vstack((X, [list_rec[i].lat, list_rec[i].lon]))

x_num = 360*3600/dist
y_num = 180*3600/dist


cluster = sklearn.DBSCAN(eps=0.0001, min_samples=5).fit(X)

print(cluster.labels_)



