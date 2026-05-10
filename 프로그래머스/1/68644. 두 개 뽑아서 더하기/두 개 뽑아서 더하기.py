def solution(nums):
    ans = set()
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            ans.add(nums[i]+nums[j])
            
    return sorted(ans)