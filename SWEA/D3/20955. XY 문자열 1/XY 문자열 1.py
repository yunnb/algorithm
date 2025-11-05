t = int(input())

for i in range(t):
    s = list(input())
    e = list(input())

    while len(e) > len(s):
        if e[-1] == 'X':
            e.pop()
        else:
            e.pop()
            e = e[::-1]

    print(f'#{i + 1}', 'Yes' if s == e else 'No')