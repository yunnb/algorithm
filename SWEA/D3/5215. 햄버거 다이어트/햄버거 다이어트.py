t = int(input())

for tc in range(1, t+1):
    n, l = map(int, input().split())
    burgers = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] * (l+1)

    for t, k in burgers:
        for cal in range(l, k-1, -1):
            dp[cal] = max(dp[cal], dp[cal-k] +t)

    print(f'#{tc} {max(dp)}')