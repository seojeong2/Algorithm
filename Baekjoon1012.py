from collections import deque
t = int(input())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    garden[i][j] = 0 #방문처리
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0<=ny<n and garden[nx][ny] == 1:
                q.append((nx,ny))
                garden[nx][ny] = 0 
                
for _ in range(t):
    m,n,k = map(int,input().split()) # m:가로길이, n: 세로길이, k: 배추심어져있는 개수

    garden = [[0] * n for _ in range(m)]
    cnt = 0

    for j in range(k):
        x,y = map(int,input().split())
        garden[x][y] = 1


    for a in range(m):
        for b in range(n):
            if garden[a][b] == 1:
                bfs(a,b)
                cnt += 1
    print(cnt)
