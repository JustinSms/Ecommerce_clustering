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

#numpy.set_printoptions(threshold=sys.maxsize)
data_matrix = Gower.distance_matrix

# SPECTRALCLUSTERING
sc = SpectralClustering(5, affinity='precomputed', n_init=100,assign_labels='discretize')
sc.fit_predict(data_matrix)

print(sc.labels_)







