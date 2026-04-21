def solution(x):
    s = sum(map(int, list(str(x))))
    
    if (x % s == 0): return True

    return False