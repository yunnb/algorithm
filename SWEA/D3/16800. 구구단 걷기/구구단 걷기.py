t = int(input())

for t in range(1, t + 1):
    n = int(input())

    ans = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            # 찾는 위치가 (x, y) 일 때, 최소이동거리는 (x-1) + (y-1)
            ans = (i - 1) + (n // i - 1)

    print(f'#{t} {ans}')
