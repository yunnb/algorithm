def solution(answers):
    ans = []
    arr = [ 
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    score = [0, 0, 0]
    for i, a in enumerate(answers):
        for j in range(3):
            if arr[j][i % len(arr[j])] == a:
                score[j] += 1 
        
    m = max(score)
    for i, s in enumerate(score): 
        if s == m:
            ans.append(i+1)
    
    return ans