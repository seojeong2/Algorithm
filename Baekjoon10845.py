from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())

queue = deque()
for _ in range(n):
    command = input().rstrip().split()

    if command[0] == "push":
        queue.append(int(command[1]))

    elif command[0] == "pop":
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif command[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])







