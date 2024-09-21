n = int(input())
coins = [500,100,50,10,5,1]

result = 0
i = 0

total = 1000 - n
while total != 0:
    cnt = total // coins[i] # 몫
    result += cnt
    total -= coins[i] * cnt
    i += 1
print(result)