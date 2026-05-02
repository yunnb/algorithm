def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    
    for e in s:
        if not e.isdigit():
            return False
            
    return True