n= int(input())
arr = list(map(int,input().split()))


def isPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

result = 0

for i in arr:
    if isPrime(i):
        result += 1
    else:
        continue

print(result)
