def solution(num):
    ans = 0
    l = len(num)
    
    for i in range(l):
        for j in range(i+1, l):
            for k in range(j+1, l):
                if num[i] + num[j] + num[k] == 0:
                    ans += 1
        
    return ans