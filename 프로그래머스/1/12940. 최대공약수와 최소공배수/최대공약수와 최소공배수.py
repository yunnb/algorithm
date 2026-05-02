import math

def solution(n, m):
    gcd = math.gcd(n, m)
    lcm = (n * m) // math.gcd(n, m)
    
    return [gcd, lcm]