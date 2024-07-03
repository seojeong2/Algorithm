import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

# 간선 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# 결과 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INF", end= " ")
        else:
            print(graph[a][b], end= " ")
    print()
