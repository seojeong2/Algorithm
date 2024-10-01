import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().rstrip().split()))
cards.sort()

m = int(input())
candidate = list(map(int,input().rstrip().split()))

card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1


def binary_search(array,target,start,end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if array[mid] == target:
        return card_count.get(target)
    elif array[mid] < target:
        return binary_search(array,target, mid+1,end)
    else:
        return binary_search(array, target, start, mid-1)

for target in candidate:
    print(binary_search(cards, target, 0, n-1), end=' ')