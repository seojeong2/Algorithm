import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = []

for _ in range(n):
    x,y = map(int,input().rstrip().split())
    arr.append((x,y))

arr = sorted(arr, key=lambda x:[x[1],x[0]])

for i in arr:
    print(i[0], i[1])