i = 0
while True:
    i += 1
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0: break

    ans = ((v // p) * l) + min(l, (v % p))

    print(f'Case {i}: {ans}')

# l p v  -> p일 중 l일 동안 사용 가능. v일 휴가
# 5 8 20
# 8일 중 5일 가능. 20일 휴가
# 8 8 4
# 20 // 8 = 2 * 5
# 20 % 8 = 4
# (20 // 8) *  5 + (20 %8)
# (v // p * l) + (v % p)

# 2 4 7 -> 7일 휴가 동안 4일마다 2일씩
# 4 3
# 2 + 2 +
# 7 // 4 = 1
# 7 % 4 = 3

# l >= v % p => v % p
# l < v % p => l
