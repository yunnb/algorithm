t = int(input())


def L(a, b):
    return a, a + b


def R(a, b):
    return a + b, b


for tc in range(1, t + 1):
    arr = list(input())
    l, r = 1, 1

    for i in arr:
        if i == 'L':
            l, r = L(l, r)
        else:
            l, r = R(l, r)

    print(f'#{tc} {l} {r}')
