from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    arr = list(map(str, input().rstrip()))
    graph.append(arr)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(a,b):
    visited[a][b] = 1
    q = deque()
    q.append([a,b])

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny < 0 or ny >= n:
                continue
            if graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx,ny])

# 적록색약 아닌 경우
visited = [[0] * n for _ in range(n)]
cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1

#print(cnt1)

# 적록색약인 경우 R == G
visited = [[0] * n for _ in range(n)]
cnt2 = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt2 += 1
#print(cnt2)

print(cnt1, cnt2)
