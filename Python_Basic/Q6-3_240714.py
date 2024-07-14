import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []
for _ in range(n):
    data = input().rstrip().split()
    arr.append((data[0], int(data[1])))

arr = sorted(arr, key=lambda x:x[1])

for i in arr:
    print(i[0], end=' ')