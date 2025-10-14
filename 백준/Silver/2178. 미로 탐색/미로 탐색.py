from collections import deque
n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dist = [[-1]*m for _ in range(n)]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서

def in_range(x, y):
    return 0<=x<n and 0<=y<m

q = deque()
q.append((0, 0))
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and maze[nx][ny] == 1 and dist[nx][ny] == -1:
            q.append((nx, ny))
            dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])