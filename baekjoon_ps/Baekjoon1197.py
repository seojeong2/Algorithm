import sys
input = sys.stdin.readline

v,e = map(int,input().split())
parent = [0] * (v+1)
edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a <b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    a,b,c = map(int,input().split())
    edges.append((c,a,b))


edges.sort()
# 간선 하나씩 확인
for edge in edges:
    cost, a,b = edge
    # 사이클 있는지 확인
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)