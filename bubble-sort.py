array = [4, 5, 6, 1, 2, 9.1, 35]

for i in range(len(array)):
    for j in range(0,len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

for i in range(len(array)):
    for j in range(0,len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]