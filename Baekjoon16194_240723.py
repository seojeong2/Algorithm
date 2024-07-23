n = int(input())
cards = list(map(int,input().split()))
cards.insert(0,0)

dp = [int(1e9)] * (n+1)
dp[0] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        dp[i] = min(dp[i], dp[i-j] + cards[j])

print(dp[n])