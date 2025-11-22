t = int(input())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for tc in range(1, t + 1):
    n = int(input())
    grid = [[0] * n for _ in range(n)]

    x, y = 0, 0
    cnt = 1
    d = 0
    for i in range(n * n):
        grid[x][y] = cnt

        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and grid[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x, y = x + dxs[d], y + dys[d]

        cnt += 1

    print(f'#{tc}')
    for g in grid:
        print(*g)
