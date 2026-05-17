def solution(n, m, section):
    ans = 0

    w = [1] * n
    for s in section:
        w[s-1] = 0
        
    i = 0
    while i < n:
        if w[i] == 0:
            ans += 1
            i += m
        else: 
            i+=1
        
    return ans