import sys
input = sys.stdin.readline

n = int(input().rstrip())
members = []

for i in range(n):
    data = input().rstrip().split()

    members.append((int(data[0]), data[1], i))

members = sorted(members, key=lambda x:[x[0],x[2]])

for i in members:
    print(i[0], i[1])