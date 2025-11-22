t = 10

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(1, n + 1):
        high = arr.index(max(arr))
        low = arr.index(min(arr))

        arr[high] -= 1
        arr[low] += 1

        if arr.count(arr[0]) == len(arr):
            break

    ans = max(arr) - min(arr)
    print(f'#{tc} {ans}')
