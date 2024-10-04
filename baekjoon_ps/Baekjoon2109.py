import heapq
n = int(input())
lectures = []
for _ in range(n):
    p,d = map(int,input().split())
    lectures.append((p,d))

lectures.sort(key=lambda x:[x[1],-x[0]])

q = []
for pay,day in lectures:
    heapq.heappush(q,pay)
    if day < len(q): # 강연일 보다 크면
        heapq.heappop(q)

print(sum(q))
