import sys
n = int(input())

x = 2
a = []

while x <= n:
    if n%x == 0:
        a.append(x)
        n //= x
    else:
        x += 1
    
for i in a:
    print(i)