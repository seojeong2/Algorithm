n = int(input())
arr = list(map(int,input().split()))

arr.sort()

result = 0 
time = 0
for i in arr:
    time += i
    result += time


print(result)