import sys
input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
dict = dict()

for _ in range(n):
    temp = input().rstrip()
    dict[temp] = 1

result = 0
for _ in range(m):
    key = input().rstrip()

    if key in dict:
        result += 1
    
print(result)