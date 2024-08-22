import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

word_dict = dict()

for _ in range(n):
    word = input().rstrip()
    if len(word) < m:
        continue
    else:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
sorted_dict = sorted(word_dict.items(), key=lambda item: (-item[1],-len(item[0]),item[0]))

for i in sorted_dict:
    print(i[0])


