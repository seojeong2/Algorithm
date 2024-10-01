n = int(input())
m = int(input())

fixed_seats = [int(input()) for _ in range(m)]

d =  [0] * (n+1)
d[0],d[1] = 1,1
d[2] = 2

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

answer = 1
last_seat = 0
for fixed in fixed_seats:
    section_size = fixed - last_seat -1
    if section_size > 0:
        answer *= d[section_size]
    last_seat = fixed

# 마지막 고정 좌석 이후의 좌석 처리

section_size = n - last_seat 
answer *= d[section_size]

print(answer)