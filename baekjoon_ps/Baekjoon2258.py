n,m = map(int,input().split())
meats = []
for _ in range(n):
    w,p = map(int,input().split())
    meats.append((w,p))

meats.sort(key=lambda x:[x[1],-x[0]]) # 가격 오름차순, 무게 내림차순

weight, same = 0,0
flag = False

answer = int(1e9)
for i in range(n):
    weight += meats[i][0] # 현재 무게더함
    if i>=1 and meats[i][1] == meats[i-1][1]: # 가격이 같은 고기가 있을경우
        same += meats[i][1]

    else:
        same = 0

    if weight >= m:
        answer = min(answer, meats[i][1] + same)
        flag = True

print(answer if flag else -1)

