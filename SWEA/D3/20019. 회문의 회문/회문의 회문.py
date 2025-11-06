t = int(input())

for t in range(1, t + 1):
    a = input()
    b = a[::-1]

    c = a[:(len(a) - 1) // 2]
    d = c[::-1]

    e = a[(len(a) - 1) // 2 + 1:]
    f = e[::-1]

    if a == b and c == d and e == f:
        ans = 'YES'
    else:
        ans = 'NO'

    print(f'#{t} {ans}')
