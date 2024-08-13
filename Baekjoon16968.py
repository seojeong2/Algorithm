cars = input()

n = len(cars)

if cars[0] == 'c':
    result = 26
else:
    result = 10

for i in range(1,n):
    if cars[i] == 'c':
        if cars[i-1] == 'c':
            result *= 25
        else:
            result *= 26

    else:
        if cars[i-1] == 'd':
            result *= 9
        else:
            result *= 10
print(result)