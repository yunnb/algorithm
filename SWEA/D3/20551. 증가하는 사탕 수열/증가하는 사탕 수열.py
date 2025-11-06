t = int(input())

for t in range(1, t + 1):
    a, b, c = list(map(int, input().split()))

    ans = 0
    while b >= c:
        b -= 1
        ans += 1

    while a >= b:
        a -= 1
        ans += 1

    if a < 1 or b < 1 or c < 1:
        ans = -1

    print(f'#{t} {ans}')
