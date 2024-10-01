a,b,c,x,y = map(int,input().split())

if a+b < 2*c:
    print(a*x + b*y)
else:
    res = 2 * c * min(x,y)
    if x >= y:
        diff = x - y
        res += min(a*diff, 2 * c * diff)
    else:
        diff = y - x
        res += min(b*diff, 2*c*diff)
    print(res)