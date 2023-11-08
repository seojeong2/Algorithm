t = int(input())

for i in range(t):
    total_y = 0
    total_k = 0

    for j in range(9):
        y,k = map(int, input().split())
        total_y += y
        total_k += k
    

    if total_y == total_k:
        print("Draw")
    elif total_y > total_k:
        print("Yonsei")
    else:
        print("Korea")