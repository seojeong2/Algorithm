import sys
input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(3)
else:
    d = [1 for _ in range(n+1)]
    d[1] = 3
    d[2] = 7

    for i in range(3,n+1):
        d[i] = (d[i-1] * 2 + d[i-2]) % 9901

    print(d[n])