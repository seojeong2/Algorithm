ㅊ

covered = 0
plank_cnt = 0 # 널판지 개수

for start,end in puddles:
    if covered >= end: # 이미 덮여있는 부분이면 넘어감
        continue

    if covered < start: # 덮지 않은 부분은 새로 덮음
        covered = start 

    needed_plank = (end - covered + l-1) // l
    plank_cnt += needed_plank

    covered += needed_plank * l

print(plank_cnt)