def solution(n):
    ans = 0
    n += 1
    while n > 1: 
        n -= 1
        if n % 2 != 0: continue
        ans += n 
            
    return ans