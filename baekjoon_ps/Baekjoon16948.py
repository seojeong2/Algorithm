from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int,input().split())

graph = [[0] * n for _ in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,2,-2,-1,1]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    # graph[x][y] = 1

    while q:
        x,y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

bfs(r1,c1)

# if graph[r2][c2] == 0:
#     print(-1)
# else:
#     print(graph[r2][c2])
print(graph[r2][c2] if graph[r2][c2] != 0 else -1)
