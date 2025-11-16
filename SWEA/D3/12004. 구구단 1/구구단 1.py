t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    ans = False
    for i in range(1, 10):
        if n % i == 0 and (n // i) < 10:
            ans = True
            break

    ans = 'Yes' if ans else 'No'
    print(f'#{tc} {ans}')
