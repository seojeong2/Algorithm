str = input()

# ( : 바르게 ) : 뒤집어서 같은방향으로 포개면 5cm / 다른방향이면 10cm

str = list(str)
first = str[0]

total = 10

for i in range(1,len(str)):
    if first == str[i]:
        total += 5
    else:
        total += 10
        first = str[i]

print(total)