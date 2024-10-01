import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
k = int(input())

for _ in range(e):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))

distance = [INF] * (v+1)

def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단경로 0
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 노드라면
            continue

        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])