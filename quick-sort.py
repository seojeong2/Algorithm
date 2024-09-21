array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면 right 와 pivot의 위치 변경
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 left와 right 변경
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)