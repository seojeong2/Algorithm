n = int(input())
student = list(map(int,input().split()))
student.sort()

INF = int(1e9)
min_val = INF

for i in range(len(student)//2):
    min_val = min(min_val, student[i] + student[-(i+1)])

print(min_val)