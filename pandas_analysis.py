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

#print(email_new.head(15))

## ADDRESS ANALYSIS

list_shortcut_states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY",]
state_list = []
somewhere_fucking_else = []
data_address = data["Address"]
#print(type(data_address))
#print(data_address.head(20))

for i in data_address:
    if "Box" in i:
        somewhere_fucking_else.append(i)
    else:
        state = i.split(",")[-1].split()[0]

        if state in list_shortcut_states:
            state_list.append(state)
        else:
            somewhere_fucking_else.append(i)

address_states_only = pd.Series(state_list)
#print(address_states_only.head(20))
print(address_states_only.describe())




