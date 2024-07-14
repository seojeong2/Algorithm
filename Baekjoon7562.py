from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    q = deque()
    q.append((startX,startY))

    while q:
        x,y = q.popleft()
        if x == endX and y == endY:
            return graph[x][y] - 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

t = int(input().rstrip())
for _ in range(t):
    l = int(input().rstrip())
    startX,startY = map(int,input().rstrip().split())
    endX,endY = map(int,input().rstrip().split())

    graph = [[0] * l for _ in range(l)]
    graph[startX][startY] = 1
    print(bfs())