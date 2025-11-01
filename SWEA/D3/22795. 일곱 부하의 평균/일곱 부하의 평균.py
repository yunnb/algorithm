t = int(input())

for _ in range(t):
    dwarfs = list(map(int, input().split()))

    m = max(dwarfs)
    s = sum(dwarfs)
    
    ans = float('inf')
    for i in range(m + 1, m + 8):
        if (sum(dwarfs) + i) / 7 == (sum(dwarfs) + i) // 7:
            ans = min(ans, i)

    print(ans)
