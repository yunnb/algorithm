t = int(input())

for t in range(1, t + 1):
    a, b, c, d = map(int, input().split())
    size = max(a, b, c, d) + 1
    arr1 = [0] * size
    arr2 = [0] * size

    for i in range(a, b):
        arr1[i] = 1

    for i in range(c, d):
        arr2[i] = 1

    ans = 0
    for n, m in zip(arr1, arr2):
        if n == 1 and m == 1:
            ans += 1

    print(f'#{t} {ans}')