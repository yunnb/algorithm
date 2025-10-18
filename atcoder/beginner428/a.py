s, a, b, x = map(int, input().split())

ans = 0
while x > 0:
    for i in range(a):
        ans += s
        x -= 1
        if x <= 0: break
    if x < 0: break

    for i in range(b):
        x -= 1
        if x <= 0: break

print(ans)

# solved
