n,m = map(int,input().split())

c =[]

for _ in range(n):
    p,l = map(int,input().split()) # p: 과목에 신청한 사람 수 l: 수강인원
    miles = list(map(int,input().split()))
    miles.sort(reverse=True)

    if p < l:
        c.append(1)
    else:
        mile = miles[l-1]
        c.append(mile)

c.sort()
res = 0
for tmp in c:
    if m - tmp >= 0:
        res += 1
        m -= tmp
print(res)