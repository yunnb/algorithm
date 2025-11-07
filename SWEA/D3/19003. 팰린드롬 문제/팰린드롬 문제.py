t = int(input())

for t in range(1, t + 1):
    n, m = map(int, input().split())
    strings = [list(input()) for _ in range(n)]

    ans = 0
    center = ''
    while strings:
        string = strings.pop()
        rev = string[::-1]

        if string == rev:
            center += ''.join(string)
            if center == center[::-1]:
                ans += m
                continue

        if rev in strings:
            rev_idx = strings.index(rev)
            strings.pop(rev_idx)
            ans += m * 2

    print(f'#{t}', ans)

# 1. abc cba -> 이렇게 뒤집어서 같은 문자열이 있다면 둘다 채택 (전체 문자열의 양옆에 배치)
# 2. ded -> 이런식으로 하나만을 뒤집었을 때 같다면 채택 (전체 문자열의 가운데에 배치)