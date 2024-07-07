# 나이트가 이동할 수 있는 범위

steps = [[-2,1],[-2,-1],[2,1],[2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]

pos = input()
y = int(ord(pos[0])) - int(ord('a')) + 1
x = int(pos[1]) # 열

count = 0

for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]

    if next_x >= 1 and next_x <=8 and next_y >= 1 and next_y <= 8:
        count += 1

print(count)



