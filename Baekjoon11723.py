import sys
input = sys.stdin.readline

n = int(input().rstrip())

s = set()

for _ in range(n):
    comm = input().rstrip().split()

    if len(comm) == 1:
        if comm[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()
    else:
        func, num = comm[0], int(comm[1])
        if func == "add":
            s.add(num)
        elif func == "remove":
            s.discard(num)
        elif func == "check":
            print(1 if num in s else 0)
        elif func == "toggle":
            if num in s:
                s.discard(num)
            else:
                s.add(num)


