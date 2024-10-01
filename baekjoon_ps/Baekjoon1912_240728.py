n = int(input())
arr = list(map(int,input().split()))
#d = [0] * (n+1)


for i in range(1,n):
    arr[i] = max(arr[i], arr[i-1] + arr[i])
print(max(arr))