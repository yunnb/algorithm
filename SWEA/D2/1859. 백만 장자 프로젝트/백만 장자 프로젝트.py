t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    b_m, b_c = 0, 0
    m = arr[-1]
    for a in arr[-2::-1]:

        if a <= m:  # a <= m : 구매
            b_m += a
            b_c += 1

        else:  # a > m : 그동안 구매한거 팔고 m 갱신
            ans += m * b_c - b_m
            b_m, b_c = 0, 0
            m = a

    # 배열 종료되면 , 그동안 구매한거 m값으로 팔기
    ans += m * b_c - b_m

    print(f'#{tc} {ans}')