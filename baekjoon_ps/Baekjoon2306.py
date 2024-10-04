n = int(input())
plus =[]
minus = []

one_cnt = 0
zero_cnt = 0

for _ in range(n):
    num = int(input())
    if num == 1:
        one_cnt += 1
    elif num < 0:
        minus.append(num)
    elif num > 0:
        plus.append(num)
    else:
        zero_cnt += 1


# 음수리스트 오름차순
minus.sort()
# 양수리스트 내림차순
plus.sort(reverse=True)

answer = one_cnt # 1을 곱하는것보다 더하는 것이 유리
# 양수먼저 처리
for i in range(0,len(plus),2):
    if i+1 < len(plus):
        answer += plus[i] * plus[i+1]
    else:
        answer += plus[i]


# 음수 처리
for i in range(0,len(minus),2):
    if i+1 < len(minus):
        answer += minus[i] * minus[i+1]
    else:
        # 음수가 홀수개수로 남으면 0을 곱해서 제거
        if zero_cnt > 0:
            answer += 0
        else:
            answer += minus[i]
print(answer)