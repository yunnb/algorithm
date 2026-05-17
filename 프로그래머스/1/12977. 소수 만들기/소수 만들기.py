from itertools import combinations

def is_prime(n):
    if n < 2: 
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: 
            return False
        
    return True

def solution(nums):
    answer = 0
    
    for comb in combinations(nums, 3):
        total = sum(comb) 
        if total % 2 == 0:
            continue
            
        if is_prime(total):
            answer += 1

    return answer