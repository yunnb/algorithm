n, k = map(int, input().split())

coins = list(int(input()) for _ in range(n))
coins.reverse()

cnt = 0
for c in coins:
    cnt += k // c
    k %= c

print(cnt)
