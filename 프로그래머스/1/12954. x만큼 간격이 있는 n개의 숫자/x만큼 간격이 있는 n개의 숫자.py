def solution(x, n):
    answer = []
    
    next = x
    for i in range(n):
        answer.append(next)
        next += x

    return answer