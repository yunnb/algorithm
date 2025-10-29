n, k = map(int, input().split())
isPrimes = [True for _ in range(n + 1)]  # 1-based
isPrimes[0], isPrimes[1] = False, False

cnt, ans = 0, 0
arr = []
for i in range(2, n + 1):
    if not isPrimes[i]: continue

    for j in range(i, n + 1, i):
        if isPrimes[j]:
            isPrimes[j] = False
            arr.append(j)
            cnt += 1

            if cnt == k:
                ans = j
                break

print(arr[k - 1])
