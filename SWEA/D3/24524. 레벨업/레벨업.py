t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = float('inf')

    for i in range(1, n - 1):
        li = [a for a in arr]
        li.pop(i)

        res = 0
        for j in range(n - 2):
            res += abs(li[j + 1] - li[j])

        ans = min(ans, res)

    print(ans)
