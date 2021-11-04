from collections import deque

k = int(input())

def bfs(v):
    visited[v] = 1
    q = deque()
    q.append(v)

    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                visited[i] = -visited[a]
                q.append(i)
            else:
                if visited[a] == visited[i]:
                    return False
    return True

for i in range(k):
    v,e = map(int,input().split())
    graph = [[] for i in range(v+1)]
    visited = [0] * (v+1)

    flg = 1

    for j in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print('그래프 형태',graph)
    for k in range(1,v+1):
        if visited[k] == 0:
            if not bfs(k):
                flg = -1
                break
    print('YES' if flg == 1 else 'NO')





