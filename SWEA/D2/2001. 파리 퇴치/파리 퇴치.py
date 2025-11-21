t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flies = 0
            for k in range(m):
                flies += sum(grid[i + k][j:j + m])

            ans = max(ans, flies)

    print(f'#{tc} {ans}')
