import pandas as pd
import numpy as np
import normalization_file
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(15))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]



# Normalized 
data_num_norm = normalization_file.data_num_norm_normfile
print(data_num_norm.head(5))


# data_num_norm is a dataframe -> we need np.ndarray
# .values transforms df into np.array (if neccessary specify needed columns with .iloc[])
x = data_num_norm.values
#print(x.shape)


# Elbow method
# wcss => within cluster sum of squares
# .inertia_ => Sum of squared distances of samples to their closest cluster center
wcss = []
for i in range(1,16):
    km = KMeans(n_clusters=i, init="k-means++", max_iter=300, n_init=10, random_state=0)
    km.fit(x)
    wcss.append(km.inertia_)

plt.plot(range(1,16), wcss)
plt.title("Elbow method")
plt.xlabel("Number of clusters")
plt.ylabel("wcss")
plt.show()


# setting up KMeans algorithm 
# init = method for initialization ("k-means++" -> smart choosing of centroids(default), could also be "random",... )
km = KMeans(n_clusters=5, init="k-means++", max_iter=300, n_init=10, random_state=0)
y_means = km.fit_predict(x)


# visualizing KMeans

plt.scatter(x[y_means == 0, 0], x[y_means == 0, 4], s = 100, c = 'pink')
plt.scatter(x[y_means == 1, 0], x[y_means == 1, 4], s = 100, c = "yellow")
plt.scatter(x[y_means == 2, 0], x[y_means == 2, 4], s = 100, c = 'cyan')
plt.scatter(x[y_means == 3, 0], x[y_means == 3, 4], s = 100, c = 'magenta')
plt.scatter(x[y_means == 4, 0], x[y_means == 4, 4], s = 100, c = 'orange')

plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:, 4], s = 50, c = 'green' , label = 'centeroid')
plt.xlabel("Avg. Session Length")
plt.ylabel("Yearly Amount Spent")
plt.show()






