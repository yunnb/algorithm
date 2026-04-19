def solution(n):
    arr = list(str(n))
    arr.sort()

    ans = 0
    for i in range(len(arr)):
        ans += int(arr[i]) * (10 ** i) 
    
    return ans