n = int(input())
arr = list(map(int,input().split()))
d = [0 for _ in range(n+1)]

for i in range(n):
    d[i] = arr[i]
    for j in range(i):
        if arr[i] > arr[j] and d[i] < d[j] + arr[i]:
            d[i] = d[j] + arr[i]

print(max(d))