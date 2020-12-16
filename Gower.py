import numpy as np
import pandas as pd
from sklearn.neighbors import DistanceMetric

# nominal:
#   1 = one feature is true and the other feature is not
#   0 = both features are true or not true

# metric:
#   d(x mj, x lj) = (| x mj - x lj |) / (max m mj - min m lj)

# ordinal:
#   need to be scaled to [0;1]
#   (i - 0.5)/ M   (M --> total number of features of m e.g. different lengths to highway from house 1,2,3,4,5 -> M = 5)
#   after being scaled ordinal variables will be measured like metric variables

#  



class Gower_distance:

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.num_list = []
        self.cat_list = []


    def gower_calculation(self):
        
        for a in self.dataframe:
            num_data = self.dataframe._get_numeric_data().columns
            self.num_list = list(num_data)

        for b in self.dataframe:
            if b in self.num_list:
                pass
            else:
                self.cat_list.append(b)

        

             



