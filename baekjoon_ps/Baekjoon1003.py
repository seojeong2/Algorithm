t = int(input())


for _ in range(t):
    # d[i] = d[i-1] + d[i-2]

    # 0이 호출된 횟수, 1이 호출된 횟수
    zero_cnt = [1,0] # 0이 호출 되는 리스트
    one_cnt = [0,1]

    n = int(input())

    if n > 1:
        for i in range(n-1):
            zero_cnt.append(zero_cnt[-1]+zero_cnt[-2])
            one_cnt.append(one_cnt[-1] + one_cnt[-2])

    print(zero_cnt[n], one_cnt[n])





