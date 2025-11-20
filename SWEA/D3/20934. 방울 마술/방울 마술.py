t = int(input())

for tc in range(1, t + 1):
    cmd = list(input().split())
    cups = cmd[0]
    k = int(cmd[1])

    idx = cups.index('o')

    if k == 0:
        print(f'#{tc} {idx}')
        continue

    start = 1 if idx == 1 else 0

    ans = 0
    if start == 0:
        ans = 0 if k % 2 == 0 else 1
    else:
        ans = 1 if k % 2 == 0 else 0

    print(f'#{tc} {ans}')
