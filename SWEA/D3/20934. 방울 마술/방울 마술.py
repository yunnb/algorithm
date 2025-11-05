t = int(input())

for t in range(t):
    s, k = input().split()
    k = int(k)
    start = s.index('o')

    if k == 0:
        ans = start
    elif start == 1:
        ans = 1 if k % 2 == 0 else 0
    else:
        ans = 0 if k % 2 == 0 else 1

    print(f'#{t + 1} {ans}')