import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.datasets import make_blobs
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
import normalization_file
from sklearn.neighbors import DistanceMetric
import pandas_analysis
import sys
import numpy
import Gower
from sklearn.neighbors import NearestNeighbors


#numpy.set_printoptions(threshold=sys.maxsize)

data = Gower.distance_matrix
print(data)




#print(data)
data_num_norm = normalization_file.data_num_norm_normfile
#print(type(data))
#plt.matshow(data)
#plt.show()

neigh = NearestNeighbors(n_neighbors=2)

nbrs = neigh.fit(data)

distances, indices = nbrs.kneighbors(data)

distances  =np.sort(distances, axis=0)

distances = distances[:,1]

plt.plot(distances)

plt.show()




dbscan = DBSCAN(eps=3.5, min_samples=5).fit(data)
clusters = dbscan.labels_
print(clusters)

colors = ['forestgreen', 'pink', 'yellow', 'red', 'tan', 'deeppink', 'olive', 'goldenrod', 'lightcyan', 'navy']
vectorizer = np.vectorize(lambda x: colors[x % len(colors)])