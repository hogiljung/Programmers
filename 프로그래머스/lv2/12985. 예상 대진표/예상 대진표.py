def solution(n,a,b):
    answer = 1

    while (a+1)//2 != (b+1)//2:
        a, b = (a+1)//2, (b+1)//2
        answer += 1
            
    return answer