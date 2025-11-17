t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for i in range(1, n - 1):
        a = [arr[i - 1], arr[i], arr[i + 1]]
        if a[1] != max(a) and a[1] != min(a):
            cnt += 1

    print(f'#{tc} {cnt}')
