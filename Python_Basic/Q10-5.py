# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v,e = map(int,input().split())
parent = [0] * (v+1)

for i in range(1,v+1):
    parent[i] = i

edges = [] # 간선담을 리스트
result = 0

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 간선 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost,a,b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)