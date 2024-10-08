from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
  
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny <0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                cnt += 1 
                visited[nx][ny] = True
                q.append((nx,ny))
    return cnt 
                
               

pictures = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            pic = bfs(i,j)
            pictures.append(pic)

            
print(len(pictures))
if len(pictures) == 0:
    print(0)
else:
    print(max(pictures))


