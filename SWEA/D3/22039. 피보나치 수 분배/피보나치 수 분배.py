t = int(input())
ans = []
for _ in range(t):
    f = [1, 1]
    n = int(input())

    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])

    if n % 3 == 1:
        ans.append('impossible')
    else:
        if n % 3 == 2:
            ans.extend('BA')
        ans.extend('BBA' * (n // 3))

    ans.append('-')

for e in ans:
    if e == '-':
        print()
        continue
    print(e, end='')
