import math

n = int(input())

for _ in range(n):
    m, n, x, y = map(int, input().split())
    ans = -1
    for k in range(x, math.lcm(m, n)+1, m):
        if (k - 1) % n + 1 == y:
            ans = k
            break
    print(ans)

# k를 구하라
# m = 10, n = 12, k = 33 일 때 y를 구하는 법
# 33 = 24 + 8 -> 33 % n = 8