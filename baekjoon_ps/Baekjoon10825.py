import sys
input = sys.stdin.readline

n = int(input().rstrip())

students = []
for _ in range(n):
    data = input().rstrip().split() # data[0]: 이름 data[1]:국어점수 data[2]: 영어점수 data[3]: 수학점수
    students.append((data[0],int(data[1]), int(data[2]), int(data[3])))

students = sorted(students, key=lambda x:[-x[1],x[2],-x[3],x[0]])

for i in students:
    print(i[0])