import pandas as pd
import numpy as np
import normalization_file


data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(5))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = data[["Email","Address","Avatar"]]

#data_num.info()
#data_num.describe()



#data_num.corr(method = "pearson")


### EMAIL ANALYSIS

email_tail_list = []
email_series = data["Email"]

for i in email_series:
    head, sep, tail = i.partition("@")
    email_tail_list.append(tail)

email_tail_series = pd.Series(email_tail_list)

"""email_tail_series.head(5)
email_tail_series.describe()
email_tail_series.value_counts().head(20)"""

tail_cat_list = []

for i in email_tail_list:
    if i == "gmail.com":
        tail_cat_list.append(1)
    elif i == "hotmail.com":
        tail_cat_list.append(2)
    elif i == "yahoo.com":
        tail_cat_list.append(3)
    else:
        tail_cat_list.append(4)

email_new = pd.Series(tail_cat_list)

#email_new.head(5)