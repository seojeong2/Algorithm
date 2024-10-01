import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int,input().split()))

    m = int(input()) # 만들어야 하는 금액

    d = [0] * (m+1)
    d[0] = 1

    for coin in coins:
        for i in range(m+1):
            if i >= coin:
                d[i] += d[i-coin]
    print(d[m])