import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
   
    lines.append(tuple(map(int,input().split())))

lines.sort()

left = lines[0][0] # x 시작점
right = lines[0][1] # y: 종료점

answer = 0
for i in range(1,n):
    if right >= lines[i][1]:
        continue

    elif lines[i][0] <= right < lines[i][1]:
        right = lines[i][1]
    elif right < lines[i][0]:
        answer += (right - left)
        left = lines[i][0]
        right = lines[i][1]

answer += (right - left)
print(answer)