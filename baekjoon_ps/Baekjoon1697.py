from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())

graph = [0] * 100001

q = deque()
q.append((n))

while q:
    x = q.popleft()
    if x == k:
        print(graph[x])
        break
    for nx in (x-1, x+1, x*2):
        if 0 <= nx <= 100000 and not graph[nx]:
            graph[nx] = graph[x] + 1
            q.append(nx)