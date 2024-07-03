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


t = int(input())
for _ in range(t):
    v = int(input())
    parent = [0] * (v+1)

    # parent 배열 자기자신으로 부모 초기화
    for i in range(1,v+1):
        parent[i] = i

    arr = list(map(int,input().split()))

    for j in range(len(arr)):
        a,b = j+1, arr[j]

        union_parent(parent, a,b)

    print(len(set(parent[1:])))
