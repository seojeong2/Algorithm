import sys
input = sys.stdin.readline

a,b = map(int, input().rstrip().split())
arrA = list(map(int,input().rstrip().split()))
arrB = list(map(int,input().rstrip().split()))

arrB.sort()

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

results = []
for x in arrA:
    result = binary_search(arrB, x, 0, len(arrB)-1)
    if result == None:
        results.append(x)
    else:
        continue
print(len(results))
results.sort()
if len(results) != 0:
    for x in results:
        print(x, end = ' ')

