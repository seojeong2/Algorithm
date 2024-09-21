from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
data = [] # 바이러스에 대한 정보

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0: # 바이러스가 존재하는 경우
            data.append((graph[i][j], 0, i, j)) # 정보 넣기

data.sort()
q = deque(data)

target_s,target_x,target_y = map(int,input().split()) # s초 뒤에 x,y에 존재하는 바이러스의 종류

while q:
    virus,s,x,y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌때까지 반복
    if s == target_s:
        break
    # 주변 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx <n and 0<=ny <n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
print(graph[target_x-1][target_y-1])