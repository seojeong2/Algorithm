n,m = map(int,input().split())
a,b,dir = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

d = [[0] * m for _ in range(n)]
d[a][b] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))


# 왼쪽으로 회전 -> 방향 바꿈
def turn_left():
    global dir
    dir -= 1

    if dir == -1:
        dir = 3

count = 1
turn_time = 0

while True:
    # 왼쪽 회전
    turn_left()
    nx = a + dx[dir]
    ny = b + dy[dir]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        a = nx
        b = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    # 네 방향 모두 갈수 없는 경우
    if turn_time == 4:
        nx = a - dx[dir]
        ny = b - dy[dir]

        # 뒤로 갈수 있다면 이동
        if array[nx][ny] == 1:
            a = nx
            b = ny
        else:
            break
        turn_time = 0

print(count)
