n = int(input())
d = [0] * (100001)
d[1] = 1
d[2] = 2

if n > 2:
    for i in range(3,n+1):
        d[i] = (d[i-1] + d[i-2]) % 15746

print(d[n])