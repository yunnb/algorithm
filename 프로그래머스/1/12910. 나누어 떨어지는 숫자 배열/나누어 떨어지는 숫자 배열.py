def solution(arr, d):
    ans = []
    
    for e in arr: 
        if (e % d == 0):
            ans.append(e)
        
    if (len(ans) == 0): ans.append(-1)
    else: ans.sort()
        
    return ans