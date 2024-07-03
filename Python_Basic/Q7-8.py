import sys
n,m = map(int,input().split())
arr = list(map(int,input().split()))

start = 0
end = max(arr)


while start <= end:
    total = 0

    mid = (start + end) // 2
    for x in arr:
        # 잘랐을때의 떡의 양을 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    else:
        result = mid # 최소의 길이로 잘랐을때까 정답,
        start = mid + 1
print(result)
