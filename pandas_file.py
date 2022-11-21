import numpy as np
import pandas as pd

#series

labels = ['a','b','c']

my_list = [10,20,30]
arr = np.array(my_list)

d = { 'a' : 10, 'b' : 20, 'c' : 30}

series = pd.Series(data=my_list, index=labels)
print(series)

