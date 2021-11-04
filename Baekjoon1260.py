from collections import deque
import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
dfs_visited = [False] * (n+1)
bfs_visited = [False] * (n+1)



for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

def dfs(v):
    dfs_visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)
def bfs(v):

    q = deque([v])
    bfs_visited[v] = True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for next in graph[now]:
            if not bfs_visited[next]:
                q.append(next)
                bfs_visited[next] = True


dfs(v)
print()
bfs(v)