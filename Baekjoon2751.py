import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    arr.append(int(input().rstrip()))

arr = sorted(arr)

for i in arr:
    print(i)