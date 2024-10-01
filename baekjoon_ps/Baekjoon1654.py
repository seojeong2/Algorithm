import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
array = []
for _ in range(n):
    array.append(int(input().rstrip()))

start = 1
end = max(array)

result = 0
while (start <= end):
    mid = (start + end) // 2

    total = 0
    for x in array:
        total += x // mid

    if total >= m:
        start = mid + 1
    else:
        end = mid -1

print(end)