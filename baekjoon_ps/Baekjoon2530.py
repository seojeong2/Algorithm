import sys

a,b,c = map(int, input().split()) # 현재시각 시, 분, 초
d = int(input()) # 요리하는데 필요한 시간 (초)

h = d // 3600 # 추가되는 시각
d %= 3600

m = d // 60 # 추가되는 분
d %= 60 # 추가되는 초

final_c = (c + d) % 60
b += ((c + d) // 60 + m)

final_b = b % 60

a += (b //60) + h
final_a = a % 24

print(final_a, final_b, final_c)


# case 1
# 14 30 0 
# 200

#  case2
# 17 40 45
# 6015

# 23 48 59
# 2515