n = int(input())
d = [0] * (n+1)
d[1] = 0
arr = [0] * (n+1)


for i in range(2,n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    arr[i] = i-1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0 and d[i//2] + 1 < d[i]:
        d[i] = d[i//2] + 1
        arr[i] = i//2       
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0 and d[i//3] + 1 < d[i]: 
        d[i] = d[i//3] + 1
        arr[i] = i//3

print(d[n])

path = [] # 경로

current = n
while current != 0:
    path.append(current)
    current = arr[current]

print(' '.join(map(str,path)))

