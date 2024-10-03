import heapq

n = int(input())
station = []
for _ in range(n):
    a,b = map(int,input().split()) # a: 성경이의 시작위치에서 주유소까지의 거리 / b: 채울수 있는 연료량
    station.append((a,b))

l,p = map(int,input().split()) #l: 성경이의 위치에서 마을까지의 거리 / p: 원래 있던 연료량

# 주유소 거리순 정렬
station.sort()

max_heap = []

curr_fuel = p
curr_pos = 0

refuel_cnt = 0
idx = 0

while curr_fuel < l: # 현재 연료로 갈 수 있는 모든 주유소를 탐색
    while idx < n and station[idx][0] <= curr_fuel:
        heapq.heappush(max_heap,-station[idx][1])
        idx += 1

    if not max_heap:
        print(-1)
        exit(0)

    curr_fuel += -heapq.heappop(max_heap)
    refuel_cnt += 1

print(refuel_cnt)
    

