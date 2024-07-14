import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    stack = []
    data = input().rstrip()
    for j in data:
        #print(j, end=' ')
        if j == '(':
            stack.append(j)
        else:
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else: # break문으로 끊기지 않고 수행됐을 경우를 처
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')