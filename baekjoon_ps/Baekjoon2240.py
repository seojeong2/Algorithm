t,w = map(int,input().split())
plums = []
for _ in range(t):
    plums.append(int(input()))
plums.insert(0,0)

dp = [[0] * (w+1) for _ in range(t+1)]

for i in range(1,t+1):
    for j in range(w+1):
        if j == 0: # 처음에는 1번 나무에서 시작
            dp[i][j] = dp[i-1][j] + (1 if plums[i]==1 else 0)
        else:
            if j % 2 == 0: # 짝수이면 1번 나무, 홀수면 2번 나무
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + (1 if plums[i]==1 else 0)
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + (1 if plums[i]==2 else 0)

print(max(dp[t]))