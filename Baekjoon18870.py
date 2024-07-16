import sys
input = sys.stdin.readline

n = int(input().rstrip())
arrX = list(map(int,input().rstrip().split()))

newArrX = list(set(arrX.copy()))
newArrX.sort() # 오름차순 정렬



def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for x in arrX:
    print(binary_search(newArrX, x, 0, len(newArrX)-1), end=' ')


