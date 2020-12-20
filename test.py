#1do the neccesary imports
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.datasets import make_blobs
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering
import normalization_file
from sklearn.neighbors import DistanceMetric
import pandas_analysis
import sys
import numpy
numpy.set_printoptions(threshold=sys.maxsize)

#2import dataset and specification


data = pd.read_csv("Ecommerce Customers.csv") 
#print(data.head(5))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]
data_num_norm = normalization_file.data_num_norm_normfile

print(data_cat["Address"].head(20))

