# # 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
import sys

t = int(input())

for i in range(t):
    str = list(input())
    score = 1

    prev = str[0]
    total = 0

    if prev == 'O': 
        total += 1

    for j in range(1,len(str)):
        if str[j] == 'O':
            if str[j] == prev: #이전것도 O그라미
                score += 1
            else: # 이전것이 동그라미 아님
                score = 1
            total += score
        prev = str[j]
        
    print(total)
        