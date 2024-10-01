n = int(input())
data = list(map(int,input().split()))

dp = [0] * (n+1)

for i in range(n):
    dp[i] = 1

    for j in range(i):
        if data[j] < data[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(max(dp))