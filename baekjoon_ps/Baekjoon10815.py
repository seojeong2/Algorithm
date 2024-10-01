import sys
input = sys.stdin.readline

n = int(input().rstrip())
cards = list(map(int,input().rstrip().split()))
cards.sort()

m = int(input().rstrip())
find_card = list(map(int,input().rstrip().split()))

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

for x in find_card:
    result = binary_search(cards,x,0,n-1)
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')