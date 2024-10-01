import sys
n = int(input())
p = list(map(int,input().split()))
d = [0] * 1001


for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        d[i] = max(d[i-j] + p[j-1],d[i])

print(d[n])