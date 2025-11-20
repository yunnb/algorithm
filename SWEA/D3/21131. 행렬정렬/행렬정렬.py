t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    chk = [True] * n
    for i, a in enumerate(grid[0], start=1):
        if i != a: chk[i - 1] = False

    cnt = 0
    for i in range(n - 1, 0, -1):
        if not chk[i]:
            cnt += 1
            for j in range(i, 0, -1):
                if chk[j]: chk[j] = False
                else: chk[j] = True

    print(cnt)