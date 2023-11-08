import sys

while True:
    n = int(input())
    a = []  # 약수넣기

    if n == -1:
        break

    for i in range(1,int(n/2) + 1):
        if n % i == 0:
            a.append(i)
        else:
            continue

    # 완전수인지 체크
    if n == sum(a):
        print(n,"=",' + '.join(map(str, a)), end=" ")
    else:
        print(n,"is NOT perfect.", end=" ")
    

