import sys
n = int(input())

students = []
for i in range(n):
    student = list(map(str, input().split()))
    students.append([student[0], int(student[1])])

students = sorted(students, key=lambda s:s[1])

for i in students:
    print(i[0], end=" ") 