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
for i in range(loops):
    deq_box.clear()

    # 돌리기전의 1차원 배열 deque()에 넣음
    deque.extend(final[i][i:m-i]) # 위
    deque.extend(final[m-i-1] )

