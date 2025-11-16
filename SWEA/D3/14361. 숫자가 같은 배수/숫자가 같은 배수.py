t = int(input())

for t in range(1, t + 1):
    N = input()
    base_sorted = sorted(N)
    n = int(N)

    ans = False
    for k in range(2, 10):
        m = n * k

        if len(str(m)) != len(N):
            continue

        if sorted(str(m)) == base_sorted:
            ans = True
            break

    ans = 'possible' if ans else 'impossible'
    print(f'#{t} {ans}')