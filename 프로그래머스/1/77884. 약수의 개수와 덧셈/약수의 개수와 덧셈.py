def cntDivisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0: 
            cnt += 1
    return cnt

def solution(left, right):
    ans = 0

    for i in range(left, right+1):
        cnt = cntDivisor(i)
        ans += i if cnt % 2 == 0 else -i
    return ans