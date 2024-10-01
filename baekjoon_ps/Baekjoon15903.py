n,m = map(int,input().split())
cards = list(map(int,input().split()))

for _ in range(m):
    cards.sort()
    total = cards[0] + cards[1]
    cards[0] = total
    cards[1] = total

print(sum(cards))