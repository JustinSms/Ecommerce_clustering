import pandas as pd
import numpy as np
import normalization_file


data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(5))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address"]]

# Normalization avg. Session Length
session_length_instance = normalization_file.Normalization(data_num["Avg. Session Length"].min(), data_num["Avg. Session Length"].max(), data_num["Avg. Session Length"])
session_length_norm = session_length_instance.normalizator()

# Normalization Time on App
time_app_instance = normalization_file.Normalization(data_num["Time on App"].min(), data_num["Time on App"].max(), data_num["Time on App"])
time_app_norm = time_app_instance.normalizator()

# Normalization Time on Website
time_website_instance = normalization_file.Normalization(data_num["Time on Website"].min(), data_num["Time on Website"].max(), data_num["Time on Website"])
time_website_norm = time_website_instance.normalizator()

# Normalization Time on Website
length_membership_instance = normalization_file.Normalization(data_num["Length of Membership"].min(), data_num["Length of Membership"].max(), data_num["Length of Membership"])
length_membership_norm = length_membership_instance.normalizator()

# Normalization Time on Website
year_amount_spent_instance = normalization_file.Normalization(data_num["Yearly Amount Spent"].min(), data_num["Yearly Amount Spent"].max(), data_num["Yearly Amount Spent"])
year_amount_spent_norm = year_amount_spent_instance.normalizator()

# new normalized dataframe
data_num_norm = pd.concat([session_length_norm,time_app_norm,time_website_norm,length_membership_norm,year_amount_spent_norm], axis=1)
data_num_norm.columns = ["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]

print(data_num_norm.head(5))