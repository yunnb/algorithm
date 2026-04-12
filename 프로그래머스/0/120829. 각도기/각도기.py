def solution(angle):
    ans = 0
    
    if angle == 180: ans = 4
    elif angle > 90: ans = 3
    elif angle == 90: ans = 2
    else: ans = 1
        
    return ans