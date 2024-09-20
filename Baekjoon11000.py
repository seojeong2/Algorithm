import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
lectures = []
for _ in range(n):
    lectures.append(list(map(int,input().rstrip().split())))

lectures.sort(key=lambda x:(x[0],x[1]))

answer = 0
heap = [lectures[0][1]] # 끝나는 시간 
for i in range(1,n):
    if heap[0]<= lectures[i][0]: # 이전 강의의 끝나는 시간 <= 다음강의 시작시간
        heapq.heappop(heap)
    heapq.heappush(heap,lectures[i][1])

print(len(heap))

