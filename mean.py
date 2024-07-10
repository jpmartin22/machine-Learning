def calculate_mean(data):
    mean=sum(data)/len(data)
    return mean

data_set={12,34,56,78,21}
mean_of_data_set=calculate_mean(data_set)
print("Mean: ",mean_of_data_set)