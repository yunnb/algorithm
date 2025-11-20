t = int(input())

for tc in range(1, t + 1):
    a, b, c = map(int, input().split())

    ans = abs(min(float(2 * b + a + c), (-2 * b + a + c) / 2))

    print('#{0:} {1:.1f}'.format(tc, ans))
