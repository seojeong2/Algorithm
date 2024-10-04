from collections import deque
n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] =1
    seaList = []

    while q:
        x,y = q.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx < n and 0<=ny <m:
                if not graph[nx][ny]:
                    sea += 1
                elif graph[nx][ny] and not visited[nx][ny]:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

        if sea > 0:
            seaList.append((x,y,sea))
    for x,y,sea in seaList:
        graph[x][y] = max(0,graph[x][y]-sea)
    return 1

# 얼음위치 찾아서 넣음
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            ice.append((i,j))
        
year = 0
while ice:
    visited = [[0] * (m) for _ in range(n)]
    delList = []
    group = 0
    for i, j in ice:
        if graph[i][j] and not visited[i][j]:
            group += bfs(i, j)
        if graph[i][j] == 0:
            delList.append((i, j))
    if group > 1:
        print(year)
        break
    ice = sorted(list(set(ice) - set(delList)))
    year += 1

if group < 2:
    print(0)