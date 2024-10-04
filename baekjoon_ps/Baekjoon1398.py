t = int(input())

coins = [1,10,25]
for _ in range(t):
    n = int(input())
    dp = [10 ** 15 for _ in range(100)]
    dp[0] = 0

    for coin in coins:
        for j in range(coin,100):
            dp[j] = min(dp[j],d[j-coin]+1)
    answer = 0 
    while n:
        answer += dp[n%100]
        n//= 100
    print(answer)