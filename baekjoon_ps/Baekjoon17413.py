import sys
input = sys.stdin.readline

stack = []


data = input().rstrip()
result = ''
check = False

# <> 사이에 있는 단어는 뒤집지 않음
for i in data:
    if i == '<':
        check = True
        # 이거 나오기 이전에 스택에 있던 내용 출력
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == '>':
        check = False
        for _ in range(len(stack)):
            result += stack.pop(0) # 넣은순서대로 빼기
    if i == ' ' and check == False:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

if stack: # 스택에 값이 남아있는 경우
    for _ in range(len(stack)):
        result += stack.pop()
print(result)
