import sys
input = sys.stdin.readline

n = int(input().rstrip())

d = [[0 for _ in range(10)] for _ in range(101)]

d[1] = [0,1,1,1,1,1,1,1,1,1]
for i in range(2,n+1):
    d[i][0] = d[i-1][1]
    d[i][9] = d[i-1][8]

    for j in range(1,9):
        d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % 1000000000

print(sum(d[n]) % 1000000000)