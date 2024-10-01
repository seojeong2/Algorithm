import sys
input = sys.stdin.readline

n = int(input().rstrip())
arrA = list(map(int,input().rstrip().split()))
arrA.sort()
def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end ) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

m = int(input().rstrip())
arrB = list(map(int,input().rstrip().split()))

for i in arrB:
    result = binary_search(arrA,i,0,n-1)
    if result == None:
        print(0)
    else:
        print(1)