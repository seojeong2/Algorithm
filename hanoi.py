def solution(n):
    answer = []

    def hanoi(src,target,inter,n):
        if n==1:
            answer.append([src,target])
        else:
            hanoi(src,inter,target,n-1)
            hanoi(src,target,inter,1)
            hanoi(inter,target,src,n-1)