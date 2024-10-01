import heapq
INF = int(1e9)

v,e = map(int,input().split())
start = int(input())

graph = [[] for i in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)


for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a->b로 가는 비용이 C라는 의미


# 다익스트라 알고리즘
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단거리 출력
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])



