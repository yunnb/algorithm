def solution(s):
    up = []
    low = []
    for e in s:
        if e.isupper(): up.append(e)
        else: low.append(e)
    
    up.sort(reverse=True)
    low.sort(reverse=True)
   
    return  ''.join(low) + ''.join(up)