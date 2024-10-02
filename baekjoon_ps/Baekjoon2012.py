import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

result = 0
for i in range(len(arr)):
    result += abs((i+1)-arr[i])

print(result)