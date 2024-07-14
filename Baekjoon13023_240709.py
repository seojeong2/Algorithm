import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n)

for _ in range(m):
    a,b = map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


# depth = 4인 관계

result = 0

def dfs(v,depth):
    global result
    if depth == 5:
        result = True
        return
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i,depth+1)
            visited[i] = False

for i in range(n):
    dfs(i,1)
    visited[i] = False
    if result:
        break
print(1 if result else 0)
