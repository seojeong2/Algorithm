import sys
n,k = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A -> 오름차순, B -> 내림차순
A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i],A[i]
print(sum(A))