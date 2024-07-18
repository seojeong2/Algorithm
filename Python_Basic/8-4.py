# 피보나치 수열 반복문 구현
d = [0] * 100

d[1] =1
d[2] = 1
n = 99

# 피보나치 함수 반복문으로 구현 - Bottom Up 다이나믹 프로그래밍
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])