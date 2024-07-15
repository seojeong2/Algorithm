import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
rices = list(map(int,input().rstrip().split()))

start = 0
end = max(rices)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in rices:
        if x > mid:
            total += x-mid

    # 떡의 양이 부족한 경우, 덜 자르기(오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
