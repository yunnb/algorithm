import math

t = int(input())

def solve(c, d):
    ans = 0

    # C+x가 d 자리일때의 y=C+x 범위를 자릿수 구간으로 순회
    xmin, xmax = 1, 9   # 1의 자리: 1, 9
    cshift = 10         # 10^1
    lower = c+1         # y 최소 (C+1)
    upper = c+d         # y 최대 (C+D)

    while xmin <= upper:
        # 이번 자릿수 구간과 [C+1, C+D] 교집합
        l = max(xmin, lower)
        r = min(xmax, upper)

        if l <= r:
            # f(C, y) = C*10^d + y (d: 현재 자릿수)
            vl = c * cshift + l
            vr = c * cshift + r
            # [vl, vr] 구간의 완전제곱수 개수
            ans += math.isqrt(vr) - math.isqrt(vl-1)

        xmin *= 10
        xmax = (xmax+1) * 10 - 1
        cshift *= 10

    return ans

out = []
for _ in range(t):
    c, d = map(int, input().split())
    out.append(str(solve(c, d)))

print("\n".join(out))