t = int(input())

for _ in range(t):
    l, r = map(int, input().split())

    print('yes' if 2 * l >= r + 1 else 'no')
