text = input()

text = text.upper()
dict = dict()

for i in text:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

max_val = [k for k,v in dict.items() if max(dict.values()) == v]

if len(max_val) > 1:
    print("?")
else:
    print(max_val[0])