n = int(input())
d = [0 for _ in range(91)]

d[1] = 1
d[2] = 1
if n > 2:
    for i in range(3,n+1):
        d[i] = d[i-2] + d[i-1]
print(d[n])