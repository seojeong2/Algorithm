n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]

move_types = ['L','R','U','D']

for plan in plans:
    # 이동 후 좌표
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny

print(x, y)