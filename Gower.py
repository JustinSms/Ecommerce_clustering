import numpy as np
import pandas as pd
from sklearn.neighbors import DistanceMetric
import pandas_analysis
import gower

data = pd.read_csv("Ecommerce Customers.csv")
#print(data.head(15))

data_num = data[["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent"]]
data_cat = pandas_analysis.email_new

data_num["Email"] = data_cat

data_new = data_num

#print(data_new.head(5))

# nominal:
#   1 = one feature is true and the other feature is not
#   0 = both features are true or not true

# metric:
#   d(x mj, x lj) = (| x mj - x lj |) / (max m mj - min m lj)

# ordinal:
#   need to be scaled to [0;1]
#   (i - 0.5)/ M   (M --> total number of features of m e.g. different lengths to highway from house 1,2,3,4,5 -> M = 5)
#   after being scaled ordinal variables will be measured like metric variables

s1 = DistanceMetric.get_metric("manhattan").pairwise(data_num[["Avg. Session Length"]])
#print(s1)

class Gower:

    def __init__(self, data, type_list, weight_list, variable_name_list):
        self.data = data
        self.type_list = type_list
        self.weight_list = weight_list
        self.variable_name_list = variable_name_list
        self.distance_list = []
        self.counter = 0

    def distance_calculator(self):
        for i in self.type_list:
            if i == "nominal":
                pass
            if i == "ordinal":
                
                df = self.data[[self.variable_name_list[self.counter]]]

                self.counter +=1
                
                numpy_array = df.to_numpy()

                unique_list = np.unique(numpy_array)

                M = np.count_nonzero(unique_list)
    
                numpy_array_norm = (numpy_array - 0.5)/M

                dist_ordinal = DistanceMetric.get_metric("manhattan").pairwise(numpy_array_norm)

                self.distance_list.append(dist_ordinal)
                
            if i == "metric":

                dist_metric = DistanceMetric.get_metric("manhattan").pairwise(self.data[[self.variable_name_list[self.counter]]])

                dist_metric = dist_metric/max(np.ptp(self.data[self.variable_name_list[self.counter]]),1)

                self.distance_list.append(dist_metric)
                #print(self.variable_name_list[self.counter])
                self.counter += 1

        #print(self.distance_list)


    def matrix_calculator(self):

        gower_top_equasion = [a*b for a,b in zip(self.distance_list,self.weight_list)]
        gower_top_equasion = sum(gower_top_equasion)

        gower = gower_top_equasion/ sum(self.weight_list)

        print(gower)



a = Gower(data_num, ["metric","metric","metric","metric","metric","ordinal"], [1,1,1,1,1,1], ["Avg. Session Length","Time on App","Time on Website","Length of Membership","Yearly Amount Spent","Email"])
a.distance_calculator()
a.matrix_calculator()


print("space")
print("space")
print("space")
print("space")
        
print(gower.gower_matrix(data_num))








       
"""a = np.array([1,2,3,4,5,6])
b = np.array([10,11,12,13,14,15])
d = np.array([2,4,6,8,10,12])

list_alph = [np.array([1,2,3,4,5,6]),np.array([10,11,12,13,14,15]),np.array([2,4,6,8,10,12])]
list_weight = [1,2,1]


c = [a*b for a,b in zip(list_alph,list_weight)]
print(type(c))
print(sum(c))"""


