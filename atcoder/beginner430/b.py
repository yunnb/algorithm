n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

patterns = set()

for i in range(n - m + 1):
    for j in range(n - m + 1):
        subgrid = tuple(tuple(grid[i + k][j:j + m]) for k in range(m))
        patterns.add(subgrid)

print(len(patterns))

# solved
