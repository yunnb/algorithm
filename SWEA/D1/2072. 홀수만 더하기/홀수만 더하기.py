t = int(input())

for tc in range(1, t + 1):
    nums = list(map(int, input().split()))

    ans = 0
    for n in nums:
        if n % 2 == 0: continue
        ans += n

    print(f'#{tc} {ans}')
