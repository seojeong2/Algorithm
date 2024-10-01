import sys
n = int(input())
p = list(map(int,input().split()))

d = [sys.maxsize] * 1001

d[0] = 0
d[1] = p[0]

for i in range(1,n+1,1):
    for j in range(1,i+1,1):
        d[i] = min(d[i-j] + p[j-1],d[i])

print(d[n])