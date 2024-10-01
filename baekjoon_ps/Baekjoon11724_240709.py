import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)



result=0

for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)