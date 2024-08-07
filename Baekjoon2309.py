arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)
fake = []

for i in range(1,len(arr)):
    for j in range(i):

        if total - arr[i] -arr[j] == 100:
            fake.append(arr[i])
            fake.append(arr[j])

            break

arr.sort()
for i in arr:
    if i not in fake:
        print(i)
            
