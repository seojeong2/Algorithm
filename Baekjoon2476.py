import sys
n = int(input())

money = 0
max_money = 0
for i in range(n):
    a,b,c = map(int,input().split())

    if a==b and b==c:
        money = 10000 + 1000 * a
    elif a != b and b != c and c != a:
        money = 100 * max(a,b,c)
    else:
        if a == b:
            money = 1000 + 100 * a
        elif b == c:
            money = 1000 + 100 * b
        elif c == a:
            money = 1000 + 100 * c
    
    max_money = max(money, max_money)

print(max_money)