from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
         

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
q = deque()

def bfs():

    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx <n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
                

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i,j))

bfs()
print(max(map(max,graph))-1)