# 퇴사 (백준-1450) 문제랑 비교했을때 N의 범위가 큼 (1<=N<=1500000)

n = int(input())
t = []
p = []
for _ in range(n):
    t1,p1 = map(int,input().split())
    t.append(t1)
    p.append(p1)

d = [0] * (n+1)
for i in range(n):
    d[i+1] = max(d[i+1], d[i])

    if i + t[i] <= n:
        d[i+t[i]] = max(d[i+t[i]], d[i] + p[i])

print(d[n])