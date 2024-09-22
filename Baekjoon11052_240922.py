n = int(input())
arr = list(map(int,input().split()))

arr.insert(0,0) # d 배열과 인덱스 맞춰주기 위함
d = [0 for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i] = max(d[i],arr[j] + d[i-j])
print(d[n])
