import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(5))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]

for counter in data_num.columns:
    sns.scatterplot(x = data_num["Yearly Amount Spent"], y = counter, data=data_num)
    plt.show()