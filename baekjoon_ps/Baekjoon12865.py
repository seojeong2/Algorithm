n,k = map(int,input().split())

weight = []
value = []

for _ in range(n):
    w,v = map(int, input().split())
    weight.append(w)
    value.append(v)

weight, value = [0] + weight, [0] +value


dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,k+1):
        if weight[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]]+value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])

