import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int,input().split())
k = int(input())

# 간선 정보 입력받을 그래프
graph = [[] for _ in range(v+1)]
# 최단 거리 저장
distance = [INF] * (v+1)

# 간선 정보 입력받기
for _ in range(e):
    a,b,c = map(int,input().split()) # a->b로 가는 비용이 c 라는 의미
    # 서로다른 두 정점 사이에 여러개의 간선이 존재할 수 있으므로 최소비용으로 업데이트
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # (비용, 노드번호) 순으로 넣
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(k)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
