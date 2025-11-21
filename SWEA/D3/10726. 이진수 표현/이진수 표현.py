t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    chk = True
    m = list(format(m, 'b'))
    m.reverse()
    
    if n > len(m):
        chk = False
    else:
        for i in range(n):
            if m[i] == '0':
                chk = False
                break

    ans = 'ON' if chk else 'OFF'
    print(f'#{tc} {ans}')
