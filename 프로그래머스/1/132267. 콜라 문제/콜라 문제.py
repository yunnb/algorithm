def solution(a, b, n):
    answer = 0

    while n >= a:
        q = n // a
        r = n % a

        n = q * b + r
        answer += q * b

    return answer