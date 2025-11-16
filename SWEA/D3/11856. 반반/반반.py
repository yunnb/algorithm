from collections import defaultdict

t = int(input())

for tc in range(1, t + 1):
    string = input()

    d = defaultdict(int)
    for s in string: d[s] += 1

    ans = True
    values = list(d.values())
    if len(values) != 2: ans = False
    
    for v in values:
        if v != 2:
            ans = False
            break

    ans = 'Yes' if ans else 'No'
    print(f'#{tc} {ans}')
