from collections import deque
import sys
input = sys.stdin.readline
n,m,r = map(int,input().rstrip().split())

arr = [input().split() for _ in range(n)]

# 빈 이차원 배열 생성 N*M 사이즈
final = [[0] * m for _ in range(n)]
deq_box = deque()

# 몇 겹으로 되어있는지 -> min(n,m) // 2 값이 겹수
loops = min(n,m) // 2
for i in range(loops): # 껍질별로 따로 처리
    deq_box.clear()

    # 돌리기전의 1차원 배열 deque()에 넣음 -> 시계방향으로 탐색
    deq_box.extend(arr[i][i:m-i]) # 위
    deq_box.extend([row[m-i-1] for row in arr[i+1:n-i-1]]) # 오른쪽
    deq_box.extend(arr[n-i-1][i:m-i][::-1]) # 아래
    deq_box.extend([row[i] for row in arr[i+1:n-i-1][::-1]]) # 왼쪽

    deq_box.rotate(-r) # 반시계방향 회전

    # 위쪽 넣어주기
    for j in range(i,m-i):
        final[i][j] = deq_box.popleft() 
    # 오른쪽
    for j in range(i+1, n-i-1):
        final[j][m-i-1] = deq_box.popleft()
    # 아래쪽
    for j in range(m-i-1, i-1,-1):
        final[n-i-1][j] = deq_box.popleft()
    for j in range(n-i-2,i,-1):
        final[j][i] = deq_box.popleft()

for line in final:
    print(" ".join(line))

