isPrime = [1 for _ in range(123460 * 2)]  # 1-based
isPrime[0], isPrime[1] = 0, 0

while True:
    n = int(input())
    if n == 0: break

    for i in range(2, (2 * n) + 1):
        if not isPrime[i]: continue

        for j in range(i * i, (2 * n) + 1, i):
            isPrime[j] = 0

    print(sum(isPrime[n + 1: (2 * n) + 1]))