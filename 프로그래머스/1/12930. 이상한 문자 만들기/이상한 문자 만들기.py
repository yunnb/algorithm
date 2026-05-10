def solution(s):
    ans = ''

    i = 0
    for e in s:
        if e == ' ':
            ans += e
            i = 0
            continue
        
        if i % 2 == 0:
            ans += e.upper()
        else:
            ans += e.lower()
                
        i += 1
        
    return ans