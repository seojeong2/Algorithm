array = [4,5,6,1,2,9,10,35]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1,len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[min_idx], array[i] = array[i], array[min_idx]

print(array)