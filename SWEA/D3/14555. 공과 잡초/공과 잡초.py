t = int(input())

for t in range(1, t + 1):
    string = input()

    ans = 0
    for i, s in enumerate(string):
        if s == '(':
            if i < len(string) and (string[i + 1] == ')' or '|'):
                ans += 1
        elif s == ')':
            if i > 0 and string[i - 1] == '|':
                ans += 1

    print(f'#{t} {ans}')
