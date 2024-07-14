import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack = []
for _ in range(n):
    comm = input().rstrip().split()
    #print(comm)
    if comm[0] == "push":
        stack.append(int(comm[1]))
    elif comm[0] == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif comm[0] == "size":
        print(len(stack))
    elif comm[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])