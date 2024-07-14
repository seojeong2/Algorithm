import sys
input = sys.stdin.readline

n,k = map(int,input().rstrip().split())
a = list(map(int,input().rstrip().split()))
b = list(map(int,input().rstrip().split()))

a = sorted(a) # 오름차순
b = sorted(b, reverse=True) # 내림차순

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))