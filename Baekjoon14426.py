import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())
sentences = []
for _ in range(n):
    sentences.append(input().rstrip())

arr = []
for _ in range(m):
    arr.append(input())

sentences.sort()
arr.sort()

result = 0
idx = 0
for i in arr:
    for j in range(idx,len(sentences)):
        if sentences[j].startswith(i):
            result += 1
            idx = j
            break

print(result)