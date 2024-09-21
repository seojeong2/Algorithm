n,m = map(int,input().split())
data = list(map(int,input().split()))
dp = [0] * (n+1)
dp[1] = data[0]
for i in range(2,n+1):
    dp[i] = dp[i-1] + data[i-1]

for _ in range(m):
    a,b = map(int,input().split())
    print(dp[b]-dp[a-1])