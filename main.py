import pandas as pd
import numpy as np
import normalization_file


data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(5))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]



# Normalized 
data_num_norm = normalization_file.data_num_norm_normfile

print(data_num_norm.head(5))

