t = int(input())

def dfs(node, cnt):
    visited[node] = 1

    for n in graph[node]:
        if visited[n] == 0:
            cnt = dfs(n,cnt+1)
    return cnt

for _ in range(t):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v) 
        graph[v].append(u)

    visited = [0] * (n+1)
    visited[1] = 0
    cnt = dfs(1,0)
    print(cnt)

