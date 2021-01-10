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
#print(data)

dbscan = DBSCAN()
clusters = dbscan.fit_predict(data)
print(clusters)
