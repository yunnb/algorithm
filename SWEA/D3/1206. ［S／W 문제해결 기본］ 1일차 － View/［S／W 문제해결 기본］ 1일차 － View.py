for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, n - 2):
        if arr[i] < arr[i - 2]: continue
        if arr[i] < arr[i - 1]: continue
        if arr[i] < arr[i + 1]: continue
        if arr[i] < arr[i + 2]: continue

        ans += arr[i] - max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])

    print(f'#{tc} {ans}')
