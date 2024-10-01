n = int(input())
p = list(map(int,input().split()))
p.insert(0,0) # p의 인덱스 0에 0값 넣음

dp = [0] *(n+1)
for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j] + p[j], dp[i])

print(dp[n])
