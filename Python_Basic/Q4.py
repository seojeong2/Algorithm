n = int(input())
data =list(map(int,input().split()))
data.sort()

target = 1
for x in data:
    if x > target:
        break
    target += x

print(target)