#Bottom Up
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

dp = [0 for i in range(n+1)]

for i in range(n):
    for j in range(i+arr[i][0], n+1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])

# Top Down
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# dp = [0 for i in range(n+1)]

# for i in range(n-1,-1,-1):
#     if i + arr[i][0] > n: # i일에 상담을 하는 것이 퇴사일을 넘기면 상담 진행 X
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1],arr[i][1] + dp[i+arr[i][0]])
# print(dp)