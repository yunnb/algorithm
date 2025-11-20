from collections import defaultdict

t = int(input())

for _ in range(t):
    tc = int(input())
    arr = list(map(int, input().split()))

    d = defaultdict(int)
    for a in arr:
        d[a] += 1

    ans = max(d, key=d.get)
    print(f'#{tc} {ans}')
