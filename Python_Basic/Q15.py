from collections import deque

n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 #  출발도시 초기화

q = deque([x])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1: # 아직 방묹ㄴ
            distance[next] = distance[now] + 1
            q.append(next)

check = False

for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)