def solution(a, b):
    answer = 0
    f, s = min(a, b), max(a, b)
    
    for i in range(f, s+1):
        answer += i
        
    return answer