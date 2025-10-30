t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]

    garo_sum, sero_sum = 0, 0
    for i in range(h):
        isLine = True
        for j in range(w):
            if grid[i][j] == '.':
                isLine = False
        if isLine: garo_sum += 1

    for j in range(w):
        isLine = True
        for i in range(h):
            if grid[i][j] == '.':
                isLine = False
        if isLine: sero_sum += 1

    if garo_sum == h and sero_sum == w:
        print(min(h, w))
    else:
        print(garo_sum + sero_sum)