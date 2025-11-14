t = int(input())

for t in range(1, t + 1):
    game = input()

    lose = 0
    for g in game:
        if g == 'x': lose += 1

    ans = 'YES' if lose < 8 else 'NO'

    print(f'#{t} {ans}')
