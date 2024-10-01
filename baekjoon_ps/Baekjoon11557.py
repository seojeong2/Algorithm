import sys

t = int(input())

for i in range(t):
    a = []
    n = int(input())
    for j in range(n):
        school, total = map(str, input().split())
        a.append([school, int(total)])
    
    a = sorted(a, key=lambda s:-s[1])
    print(a[0][0])