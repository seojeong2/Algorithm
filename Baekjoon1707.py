from collections import deque
import sys
input = sys.stdin.readline

#

K = int(input())
for i in range(K):

    V,E = map(int,input().split())
    graph = [[] for _ in range(V + 1)]
    color = [0] * (V + 1)

    for i in range(E):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)

    # 인접리스트는 정렬해줘야함
    for i in range(1,V+1):
        graph[i].sort()

    def bfs(v):
        color[v] = 1
        q = deque([v])
        while q:
            now = q.popleft()
            for next in graph[now]:
                if color[next] == 0:
                    color[next] = -color[now]
                    q.append(next)
                else:
                    if color[next] == color[now]:
                        return False
        return True

    isTrue = True
    for i in range(1,V+1):
        if color[i] == 0:
            if not bfs(i):
                isTrue = False
                break
    print('YES' if isTrue else 'NO')



