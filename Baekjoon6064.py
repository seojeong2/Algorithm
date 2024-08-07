import sys

input = sys.stdin.readline

def calculate(m,n,x,y):
    k = x
    while k <= m*n:
        if (k-x) % m == 0 and (k-y) % n == 0:
            return k
        k += m
    return -1

t = int(input().rstrip())
for _ in range(t):
    m,n,x,y = map(int,input().rstrip().split())
    print(calculate(m,n,x,y))
