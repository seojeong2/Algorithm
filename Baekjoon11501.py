t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))
    money = 0 # 이익
    maxPrice = 0 # 주식의 최대 가격

    for i in range(len(prices)-1,-1,-1):
        if prices[i] > maxPrice:
            maxPrice = prices[i]
        else:
            money += maxPrice - prices[i]
    print(money)
