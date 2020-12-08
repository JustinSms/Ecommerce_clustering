import pandas as pd
import numpy as np
import normalization_file
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt




data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(15))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]



# Normalized 
data_num_norm = normalization_file.data_num_norm_normfile

#print(data_num_norm.head(15))

kmeans = KMeans(n_clusters=3)
kmeans.fit(data_num_norm)

#plt.scatter(data_num_norm["Avg. Session Length"], data_num_norm["Time on Website"], )


# Scaling the data to normalize
model = KMeans(n_clusters=5).fit(data_num_norm)

# Visualize it:
plt.figure(figsize=(8, 6))
plt.scatter(data_num_norm[:,0], data_num_norm[:,1], c=model.labels_.astype(float))


