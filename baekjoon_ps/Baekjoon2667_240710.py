from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

visited = [[0] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global nums

    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    nums += 1

    while q:
        i,j = q.popleft()
        for k in range(4):
            ni = i + dx[k]
            nj = j + dy[k]

            if ni < 0 or ni >=n or nj <0 or nj >=n:
                continue
            if graph[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
                nums += 1

numList = []
nums = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j)
            numList.append(nums)
            nums = 0

print(len(numList))
numList.sort()
for i in numList:
    print(i)