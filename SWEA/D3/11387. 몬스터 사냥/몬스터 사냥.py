t = int(input())

for tc in range(1, t + 1):
    d, l, n = map(int, input().split())

    ans = 0
    for i in range(n):
        ans += d + (d * i * l) // 100

    print(f'#{tc} {ans}')

# 기본 데미지: d
# 레벨 l: d((1+n) * l/100
