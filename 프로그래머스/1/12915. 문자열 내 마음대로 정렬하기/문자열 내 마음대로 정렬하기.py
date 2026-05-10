def solution(strs, n):
    for i in range(len(strs)):
        for j in range(len(strs)-1):             
            if strs[j][n] > strs[j+1][n]:
                strs[j], strs[j+1] = strs[j+1], strs[j]
            
            if strs[j][n] == strs[j+1][n]:
                if strs[j] > strs[j+1]:
                    strs[j], strs[j+1] = strs[j+1], strs[j]
    return strs


