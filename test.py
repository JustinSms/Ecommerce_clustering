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

#print(type(data_num))

"""data_email = pandas_analysis.email_new
#data_email = pd.DataFrame(pandas_analysis.email_new)
print(type(data_email))
print(data_email.head(5))

dummy_df = pd.get_dummies(data_email)

print(dummy_df)


#s3 = DistanceMetric.get_metric('dice').pairwise(data_email)
#print(s3)"""


data_test = pd.Series([1,2,3,4,4])
# data_test = pandas_analysis.email_new

print(data_test)

dummy_test = pd.get_dummies(data_test)

print(dummy_test)

s4 = DistanceMetric.get_metric('dice').pairwise(dummy_test)
print(type(s4))
print(s4)

























""" a = np.array([1,2,3,4,5,6])
b = np.array([10,11,12,13,14,15])
d = np.array([2,4,6,8,10,12])

list_alph = [np.array([1,2,3,4,5,6]),np.array([10,11,12,13,14,15]),np.array([2,4,6,8,10,12])]
list_weight = [1,2,1]


c = [a*b for a,b in zip(list_alph,list_weight)]
print(type(c))
print(sum(c))
 """






#print(type(a))




"""x= data_num_norm.iloc[:,[3,4]].values

counter=['single', 'complete', 'average'] #list for distance methods

#3using the denrogram to find optimal number of clusters 


for i in counter: #order: single, complete, average 
    dendrogram = sch.dendrogram(sch.linkage(x, method=i))
    plt.title(i)
    plt.show()



#4fitting hierarchical clustering to the dataset 
hc = AgglomerativeClustering(n_clusters=6, affinity='euclidean',linkage='ward')
y_hc= hc.fit_predict(x)

#5visualize clusters 

plt.scatter(x[y_hc == 0, 0], x[y_hc == 0, 1], s = 50, c = 'pink')
plt.scatter(x[y_hc == 1, 0], x[y_hc == 1, 1], s = 50, c = "yellow")
plt.scatter(x[y_hc == 2, 0], x[y_hc == 2, 1], s = 50, c = 'cyan')
plt.scatter(x[y_hc == 3, 0], x[y_hc == 3, 1], s = 50, c = 'magenta')
plt.scatter(x[y_hc == 4, 0], x[y_hc == 4, 1], s = 50, c = 'orange')
plt.scatter(x[y_hc == 5, 0], x[y_hc == 5, 1], s = 50, c = 'blue')


plt.title("HC Clustering")
plt.xlabel("Length of Membership")
plt.ylabel("Yearly Amount Spent")

plt.show()"""


for i in data:
    num = data._get_numeric_data().columns
    #df = pd.DataFrame(num)
    #list(num)

#print(list(num))
#print(type(num))


