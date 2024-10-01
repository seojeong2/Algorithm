n,k = map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

d = [0] * (k+1)
d[0] = 1
for coin in coins:
    for i in range(k+1):
        if i >= coin:
            d[i] += d[i-coin]

print(d[k])