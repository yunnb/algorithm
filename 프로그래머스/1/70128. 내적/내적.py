def solution(a, b):
    answer = 0
    
    for n, m in zip(a, b):
        answer += n * m  
        
    return answer