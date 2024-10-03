x,y,w,s = map(int,input().split())

# 1. 직선으로만 이동
case1 = (x+y) * w

# 2. 최대한 대각선 , 남은거리 직선
case2 = min(x,y) * s + abs(x-y) * w

# 3. 대각선 + 직선 같이 고려
case3 = max(x,y) * s if (x+y) % 2 == 0 else (max(x,y)-1) * s + w

print(min(case1,case2,case3))