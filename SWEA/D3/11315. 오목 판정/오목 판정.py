t = int(input())


def has_five(line):
    for i in range(len(line) - 5 + 1):
        l = line[i:i + 5]
        if l.count('o') == 5: return True
    return False


for tc in range(1, t + 1):
    n = int(input())
    grid = [list(input()) for _ in range(n)]

    chk = False
    cnt = 0
    for g in grid:
        if has_five(g):
            chk = True
            break

    if not chk:
        for g in zip(*grid):
            if has_five(g):
                chk = True
                break

    if not chk:
        for i in range(n - 5 + 1):
            if chk: break
            for j in range(n - 5 + 1):
                if chk: break
                line = [grid[i + k][j + k] for k in range(5)]
                if has_five(line):
                    chk = True
                    break

    if not chk:
        for i in range(n - 5 + 1):
            if chk: break
            for j in range(n - 1, 3, -1):
                if chk: break
                line = [grid[i + k][j - k] for k in range(5)]
                if has_five(line):
                    chk = True
                    break

    ans = 'YES' if chk else 'NO'
    print(f'#{tc} {ans}')
