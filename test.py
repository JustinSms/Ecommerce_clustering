#1do the neccesary imports
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
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AffinityPropagation
from numpy.linalg import inv
from itertools import cycle
from sklearn import metrics

#numpy.set_printoptions(threshold=sys.maxsize)
data_matrix = Gower.data_matrix_gower

## 1 - GM
data_similarity_matrix = 1 - data_matrix
#print(data_similarity_matrix)
data_num_norm = normalization_file.data_num_norm_normfile



## Affinity Propagation
"""af = AffinityPropagation().fit(data_similarity_matrix)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)"""

## PCA 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

x = StandardScaler().fit_transform(data_num_norm)

pca = PCA(n_components=2)

principal_components = pca.fit_transform(x)

principal_df = pd.DataFrame(data= principal_components, columns= ["principal component 1","principal component 2"])

colors = ["red","green","blue","orange","yellow","black","grey","purple","pink"]

## Visualisation
"""import matplotlib.pyplot as plt 
from itertools import cycle 
  
plt.close('all') 
plt.figure(1) 
plt.clf() 
  
colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk') 
  
for k, col in zip(range(n_clusters_), colors): 
    class_members = labels == k 
    cluster_center = data_similarity_matrix[cluster_centers_indices[k]] 
    plt.plot(data_similarity_matrix[class_members, 0], data_similarity_matrix[class_members, 1], col + '.') 
    plt.plot(cluster_center[0], cluster_center[1], 'o', 
             markerfacecolor = col, markeredgecolor ='k', 
             markersize = 14) 
  
    for x in data_similarity_matrix[class_members]: 
        plt.plot([cluster_center[0], x[0]],  
                 [cluster_center[1], x[1]], col) 
  
plt.title('Estimated number of clusters: % d' % n_clusters_) 
plt.show() """




