import math
h,w,n,m = map(int,input().split())

# 한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때, 
# 모든 참가자는 세로로 N칸 또는 가로로 M칸 이상 비우고 앉아야 한다. 즉, 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 가로줄 번호의 차가 M보다 큰 곳에만 앉을 수 있다.

a = math.ceil(h/(n+1)) # 세로에 몇명이 앉는지
b = math.ceil(w/(m+1)) # 가로에 몇명이 앉는지

print(a*b)
