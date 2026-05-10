def solution(t, p):
    ans = 0
    tl, pl = len(t), len(p)
    
    for i in range(tl-pl+1):
        if p >= t[i:i+pl]:
            ans += 1

    return ans