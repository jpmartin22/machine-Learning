def calculate_median(data):
    data.sort()
    n=len(data)
    mid=n // 2

    if n%2==0:
        median=(data[mid-1]+data[mid])/2
    else:
        median=data[mid]
    return median
data_set=[12,34,56,78,21]
#data_set.sort()
median_of_data_set=calculate_median(data_set)
print("Median: ",median_of_data_set)