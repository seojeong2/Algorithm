import sys
input = sys.stdin.readline

n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]

for i in range(n):
    data = list(map(int,input().rstrip()))
    graph.append(data)

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y):
    global nums
    visited[x][y] = 1

    if graph[x][y] == 1:
        nums += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny < n:
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx,ny)
numList = []
nums = 0
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            dfs(x,y)
            numList.append(nums)
            nums = 0
print(len(numList))
numList.sort()
for i in numList:
    print(i)




