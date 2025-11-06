t = int(input())

for t in range(1, t + 1):
    n, m = map(int, input().split())
    narr = list(input().split())
    marr = list(input().split())
    q = int(input())
    years = [int(input()) for _ in range(q)]

    ans = []
    for y in years:
        ans.append(narr[(y - 1) % n] + marr[(y - 1) % m])

    print(f'#{t}', *ans)
