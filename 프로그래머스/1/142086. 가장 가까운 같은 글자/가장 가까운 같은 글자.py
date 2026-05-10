def solution(s):
    ans = []
    dic = {}
    
    for i, e in enumerate(s):
        if e not in dic: ans.append(-1)
        else: ans.append(i - dic[e])
        dic[e] = i
        
    return ans