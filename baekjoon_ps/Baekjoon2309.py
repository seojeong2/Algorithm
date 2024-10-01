arr = []
for _ in range(9):
    arr.append(int(input()))

total = sum(arr)
fake = []

for i in range(9):
    for j in range(i+1,9):
        if len(fake) == 2:
            continue
 
        if total - arr[i] -arr[j] == 100:
            fake.append(arr[i])
            fake.append(arr[j])
            

arr.sort()
for i in arr:
    if i not in fake:
        print(i)
            
