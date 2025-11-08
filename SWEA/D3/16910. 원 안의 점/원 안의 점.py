t = int(input())

for t in range(1, t + 1):
    n = int(input())

    ans = 0
    for x in range(n + 1):
        for y in range(n + 1):
            if x ** 2 + y ** 2 <= n ** 2:
                if x == 0 and y == 0: ans += 1
                elif x == 0 or y == 0: ans += 2
                else: ans += 4

    print(f'#{t} {ans}')
