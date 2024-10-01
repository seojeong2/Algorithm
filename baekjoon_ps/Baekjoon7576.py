from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().rstrip().split())
boxes = []

for _ in range(n):
    boxes.append(list(map(int,input().rstrip().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

q = deque()

# 초기값
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            q.append((i,j))



def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >=n or ny <0 or ny >=m:
                continue
            if boxes[nx][ny] == -1:
                continue

            if boxes[nx][ny] == 0:
                boxes[nx][ny] = boxes[x][y] + 1
                q.append((nx,ny))

bfs()

result = 0

for i in boxes:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    result = max(result,max(i))

print(result - 1)
