n, m = map(int, input().split())
paper = [ list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

painting_cnt = 0
max_width = 0

def in_range(x, y):
    return 0<=x<n and 0<=y<m

def explore(i, j):
    visited[i][j] = True
    stk = [(i, j)]
    width = 1

    while stk:
        x, y = stk.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and paper[nx][ny] == 1 and not visited[nx][ny]:
                stk.append((nx, ny))
                visited[nx][ny] = True
                width += 1
    return width

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            max_width = max(explore(i, j), max_width)
            painting_cnt += 1

print(painting_cnt, max_width, sep='\n')