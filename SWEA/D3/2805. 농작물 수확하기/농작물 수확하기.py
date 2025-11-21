from collections import deque

t = int(input())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input())) for _ in range(n)]
    dist = [[-1] * n for _ in range(n)]

    c = n // 2

    q = deque()
    q.append((c, c))
    dist[c][c] = 0

    ans = grid[c][c]
    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1

                if dist[nx][ny] <= c:
                    ans += grid[nx][ny]
                    q.append((nx, ny))

    print(f'#{tc} {ans}')
