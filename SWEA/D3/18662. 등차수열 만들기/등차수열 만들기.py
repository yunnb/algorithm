t = int(input())

for t in range(1, t + 1):
    a, b, c = map(int, input().split())

    ans = abs(((2 * b) - a - c) / 2.0)
    print(f'#{t} {ans:.1f}')
