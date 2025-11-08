t = int(input())

for t in range(1, t + 1):
    a, b = map(int, input().split())
    ans = 1
    if a == b: ans = a
    print(f'#{t} {ans}')
