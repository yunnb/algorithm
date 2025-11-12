t = int(input())

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for t in range(1, t + 1):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(n)]

    ans = True
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '?': continue

            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if not in_range(nx, ny): continue
                if grid[nx][ny] == '?': grid[nx][ny] = '#' if grid[i][j] == '.' else '.'
                elif grid[nx][ny] == grid[i][j]: ans = False

        if not ans: break

    ans = ('' if ans else 'im') + 'possible'
    print(f'#{t} {ans}')