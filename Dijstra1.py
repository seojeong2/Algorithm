import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)
distance = [INF] * (v+1)

start = int(input())
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0

    for i in range(1,v+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index 

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1]

    # 시작 노드를 제외한 전체 v-1개의 노드에 대해 반복
    for i in range(v-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

