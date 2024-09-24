# 1) 현재 있는 칸과 다음칸의 좌표차이 비교 (2,1) (1,2)
# 2) 방문하지 않은 칸 있는지 확인
# 3) 마지막 칸과 출발한 칸의 좌표차이가 (2,1) (1,2)

def check_valid(now,dist):
    if abs(ord(now[0])-ord(dist[0])) == 2 and abs(int(now[1]) - int(dist[1])) == 1:
        return 1
    elif abs(ord(now[0]) - ord(dist[0])) == 1 and abs(int(now[1])-int(dist[1])) == 2:
        return 1
    else:
        return 0

arr = []
now = input()
arr.append(now)
cnt = 1
for i in range(35):
    dest = input()
    arr.append(dest)

    if check_valid(now,dest) == 1:
        cnt += 1
        now = dest
    else:
        break

if cnt == 36 and len(set(arr)) == 36 and check_valid(arr[-1],arr[0]) == 1:
    print("Valid")
else:
    print("Invalid")