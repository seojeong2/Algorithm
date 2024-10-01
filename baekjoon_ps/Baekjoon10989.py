import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [0] * 10001
for _ in range(n):
    data = int(input().rstrip())
    arr[data] += 1

for i in range(len(arr)):
    for j in range(arr[i]):
        print(i)