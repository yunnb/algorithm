t = int(input())

for t in range(1, t + 1):
    n = int(input())
    days = list(map(int, input().split()))

    ans = float('inf')
    for i in range(7):
        if days[i] == 0: continue

        day, cnt = 0, 0
        while day < n:
            day += days[i]
            cnt += 1
            i += 1
            if i == 7: i = 0

        ans = min(ans, cnt)

    print(f'#{t} {ans}')
