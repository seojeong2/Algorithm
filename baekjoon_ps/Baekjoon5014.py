from collections import deque
f,s,g,u,d = map(int,input().split())

visited = [0] * (f + 1)

def bfs():
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        x = q.popleft()

        if x == g:
            return visited[x] - 1
        for i in [u,-d]:
            move = x + i
            if 0< move <= f and visited[move] == 0:
                visited[move] = visited[x] + 1
                q.append(move)
    return "use the stairs"


print(bfs())
