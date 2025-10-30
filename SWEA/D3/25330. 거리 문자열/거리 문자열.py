t = int(input())


def is_valid(s):
    first_pos = [-1] * 10
    cnt = [0] * 10

    for i, e in enumerate(s):
        cnt[e] += 1

        if cnt[e] == 1:  # 첫 방문
            first_pos[e] = i
        elif cnt[e] == 2:
            if i - first_pos[e] - 1 != e:
                return False
        else:  # 해당 숫자 3개 이상
            return False

    return all(c in (0, 2) for c in cnt)


for _ in range(t):
    s = list(map(int, input().strip()))

    print('yes' if is_valid(s) else 'no')