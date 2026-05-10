def solution(sizes):
    ma, mb = 0, 0
    for s in sizes:
        a, b = max(s[0], s[1]), min(s[0], s[1])
        ma, mb = max(a, ma), max(b, mb)
    
    return ma * mb