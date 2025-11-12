t = int(input())

ans = []
for _ in range(t):
    board = [list(input()) for _ in range(8)]
    chk = True

    for i in board:
        cnt = i.count('O')
        if cnt != 1:
            chk = False
            break

    for i in zip(*board):
        cnt = i.count('O')
        if cnt != 1:
            chk = False
            break

    if chk: ans.append('yes')
    else: ans.append('no')

for i, a in enumerate(ans, start=1):
    print(f'#{i} {a}')