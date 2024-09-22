array = [4, 5, 6, 1, 2, 9.1, 35]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

