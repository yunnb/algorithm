def solution(absol, signs):
    ans = 0
    
    for a, s in zip(absol, signs):
        if s: ans += a
        else: ans -= a
            
    return ans