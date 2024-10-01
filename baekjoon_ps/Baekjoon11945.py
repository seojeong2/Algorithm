import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(input().rstrip())

for i in range(len(arr)):
    print(arr[i][::-1])

