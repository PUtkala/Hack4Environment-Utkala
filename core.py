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

for i in range(len(x.features)):
    list_rec.append(Record(i, x.features[i].properties))
    X = np.vstack((X, [list_rec[i].lat, list_rec[i].lon]))

X = X[1:-1]

cluster = sklearn.DBSCAN(eps=0.0001, min_samples=100).fit(X)

#print(cluster.labels_)

cluster_count = np.unique(cluster.labels_)-1
for i in range(len(list_rec)-1):
    if cluster.labels_[i] != -1:
        list_rec[i].color = color_list[cluster.labels_[i]%6]
    plt.plot(X[i,1],X[i,0], list_rec[i].color)
    plt.grid("on")

plt.show()

