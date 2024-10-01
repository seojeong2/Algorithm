import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split()) # x가 시작점
graph = [[] for _ in range(n+1)]
#distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance

# X번 마을에서 각자의 마을까지 최단거리
ans = dijkstra(x)
ans[0] = 0 # 0번노드 초기화
for i in range(1,n+1):
    if i != x: # x번 노드는 제외
        dis = dijkstra(i)
        ans[i] += dis[x]
print(max(ans))

