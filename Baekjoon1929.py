# M이상 N이하 소수 모두 구하는 프로그램
import math
m,n = map(int,input().split())

primes = []
for i in range(m,n+1):

    if i == 1:
        continue
    for j in range(2,math.sqrt(i,2)+1):
        if i % j == 0:
            break
    else:
        print(i)

