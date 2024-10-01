n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort()
answers = []

for x in data:
    answers.append(x * n)
    n-=1

print(max(answers))