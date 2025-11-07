t = int(input())

for t in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    chk = [[False] for _ in range(n * 2)]

    ans = []
    while arr:
        cur = arr.pop()
        sale = int(cur * 0.75)

        if sale in arr:
            idx = arr.index(sale)
            ans.append(arr[idx])
            arr.pop(idx)

    print(f'#{t}', *ans[::-1])
