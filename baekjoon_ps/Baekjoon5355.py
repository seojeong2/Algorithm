import sys

n = int(input())

for i in range(n):

    result = 0
    str = input().split(" ")

    result += float(str[0])

    for j in range(1,len(str)):
        if j == '@':
            result *= 3
        elif j == '%':
            result += 5
        else:
            result -= 7

    print(f"{result:.2f}")
