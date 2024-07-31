a,b = map(int,input().split())

def gcd(x,y):
   tmp = x % y
   x = y
   y = tmp

   if tmp == 0:
       return x
   else:
       return gcd(x,y)

print(gcd(a,b))
print(a*b // gcd(a,b))
