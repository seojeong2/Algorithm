n= int(input())
arr = list(map(int,input().split()))

d = [0 for _ in range(n+1)]

for i in range(n):
    d[i] = 1
    for j in range(i):
        if arr[j] < arr[i] and d[i] < d[j] + 1:
            d[i] = d[j] + 1

#print(d)
print(max(d))