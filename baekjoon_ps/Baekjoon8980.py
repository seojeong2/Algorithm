import sys
input = sys.stdin.readline

n,c = map(int,input().rstrip().split())
m = int(input().rstrip())
infos = []
for _ in range(m):
    s,r,box = map(int,input().rstrip().split())
    infos.append((s,r,box))
infos.sort(key=lambda x:x[1]) # 도착마을 기준으로 오름차순 정렬

capacity = [c] * n
total = 0

for s,r,box in infos:
    _min = c
    for i in range(s,r):
        if _min > min(capacity[i], box):
            _min = min(capacity[i], box)
    for i in range(s,r):
        capacity[i] -= _min
    total += _min
print(total)