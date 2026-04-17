def solution(n):
    arr = []
    
    for i in range(n, 0, -1):
        if n % i != 0: continue
        arr.append(i)
        
    return sum(arr)