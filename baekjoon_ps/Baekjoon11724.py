import sys
sys.setrecursionlimit(10000)

n,m = map(int,sys.stdin.readline().split())
adj = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
count = 0

def dfs(v):
    visited[v] = 1
    for k in range(1,n+1):
        if adj[v][k] ==1 and visited[k] == 0:
            dfs(k)

for i in range(m):
    u,v = map(int,sys.stdin.readline().split())
    adj[u][v] = 1
    adj[v][u] = 1

for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        count += 1
print(count)

