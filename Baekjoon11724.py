import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort()

def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if not visited[next]:
            dfs(next)

count = 0
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        count += 1
print(count)