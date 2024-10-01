n = int(input())
plus = [] 
minus = [] # 입력받을때부터 양수, 음수 나눠서 저장

result = 0
for _ in range(n):
    num = int(input())

    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

# 정렬
plus.sort(reverse=True) # 내림차순 정렬
minus.sort() # 오름차순 정렬

# 양수 묶기
for i in range(0,len(plus),2):
    if i+1 >= len(plus):
        result += plus[i]
    else:
        result += (plus[i] * plus[i+1])

# 음수 묶기
for i in range(0, len(minus), 2):
    if i+1 >= len(minus):
        result += minus[i]
    else:
        result += (minus[i] * minus[i+1])

print(result)


