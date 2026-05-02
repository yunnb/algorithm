def solution(arr1, arr2):
    answer = []
    
    for n, m in zip(arr1, arr2):
        row = []
        
        for i in range(len(n)):
            row.append(n[i] + m[i])
            
        answer.append(row)
        
    return answer