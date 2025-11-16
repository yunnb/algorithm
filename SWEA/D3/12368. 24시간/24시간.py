t = int(input())

for tc in range(1, t + 1):
    s, e = map(int, input().split())
    print(f'#{tc} {(s + e) % 24}')
