import sys
input = sys.stdin.readline

r,c=map(int,input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

canGo = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == "W":
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    continue
                if graph[nx][ny] == "S":
                    canGo = True
                    break
if canGo:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'D'
    for k in graph:
        print(''.join(k))

