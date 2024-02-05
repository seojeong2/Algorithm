n = int(input())

loss = list(map(int,input().split()))
joy = list(map(int,input().split()))

loss, joy = [0] + loss, [0] + joy

# dp = [[0 for _ in range(101)] for _ in range(n+1)]

# for i in range(1,n+1):
#     for j in range(1,101):
#         if loss[i] <= j: # 잃는 체력이 100이하이면
#             dp[i][j] = max(dp[i-1][j],dp[i-1][j-loss[i]] + joy[i])
#         else:
#             dp[i][j] = dp[i-1][j]


dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        if loss[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-loss[i]] + joy[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][99])
