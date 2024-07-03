from collections import deque


n = int(input())
visited = [False] * (n+1)
answer = [0] * (n+1)

edges = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    edges[a].append(b)
    edges[b].append(a)


def bfs(edges,v,visited):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for i in edges[x]:
            if not visited[i]:
                answer[i] = x
                q.append(i)
                visited[i] = True

bfs(edges, 1,visited)
for i in range(2,n+1):
    print(answer[i])