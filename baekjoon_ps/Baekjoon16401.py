import sys
input = sys.stdin.readline

m,n = map(int,input().rstrip().split())
snacks = list(map(int,input().rstrip().split()))

snacks.sort()
start = 1
end = int(1e9)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in snacks:
        if x >= mid:
            total += (x // mid)

    if total < m:
        end = mid -1
    else:
        result = max(mid,result)
        start = mid + 1

print(result)



