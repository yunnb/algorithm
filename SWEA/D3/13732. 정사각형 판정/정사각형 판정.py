t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)

    ans = True
    if max_x - min_x != max_y - min_y:
        ans = False

    for i in range(min_y, max_y + 1):
        for j in range(min_x, max_x + 1):
            if grid[i][j] == '.':
                ans = False
                break

    ans = 'yes' if ans else 'no'
    print(f'#{tc} {ans}')
