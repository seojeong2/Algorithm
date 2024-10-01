import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
result = 0

def dfs(start,depth):
    global result
    if depth == 5:
        result = True
        return
    visited[start] = True
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(next_node,depth + 1)
            visited[next_node] = False

result = False
for i in range(n):

    dfs(i,1)
    visited[i] = False
    if result:
        break
print(1 if result else 0)


