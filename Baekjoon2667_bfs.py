from collections import deque
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

def bfs(x,y):
    global nums
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    nums += 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx <0 or nx >= n or ny <0 or ny >= n:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                nums += 1
numList = []
nums = 0

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1 and visited[x][y] == 0:
            bfs(x,y)
            numList.append(nums)
            nums = 0

print