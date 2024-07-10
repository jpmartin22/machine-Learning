import numpy as np

def calculate_percentile(data,percentile):
    return np.percentile(data,percentile)

data_set=[10,15,20,25,30]
percentile_result=calculate_percentile(data_set,75)
print("75th percentile is: ",percentile_result)