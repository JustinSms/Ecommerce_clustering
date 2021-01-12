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


#numpy.set_printoptions(threshold=sys.maxsize)

data = Gower.data_matrix_gower

data_real = pandas_analysis.data_real


from scipy.spatial.distance import squareform, pdist

print(pd.DataFrame(squareform(pdist(data_real[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]))))
