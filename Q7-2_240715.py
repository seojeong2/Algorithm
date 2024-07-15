import sys
input = sys.stdin.readline

n = int(input())
stocks = list(map(int,input().rstrip().split()))

m = int(input())
wants = list(map(int,input().rstrip().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

for i in wants:
    result = binary_search(stocks, i, 0, n-1)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')