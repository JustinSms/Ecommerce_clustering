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
#numpy.set_printoptions(threshold=sys.maxsize)


data = Gower.data_matrix_gower
print(data)
#print(type(data))
#plt.matshow(data)
#plt.show()



dbscan = DBSCAN()
clustering = DBSCAN(eps=0.002, min_samples=2).fit(data)
clusters = clustering.labels_


#print(clusters)
