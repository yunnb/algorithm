t = int(input())

for _ in range(t):
    a, b, n = map(int, input().split())

    x, y = a, b
    cnt = 0
    while x <= n and y <= n:
        cnt += 1
        if x >= y:
            y += x
        else:
            x += y

    print(cnt)
