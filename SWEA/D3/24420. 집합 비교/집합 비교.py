t = int(input())


def is_same(a, b):
    return True if a == b else False


def is_part(a, b):  # b는 a의 부분인가 !
    cnt = 0
    for i in range(len(b)):
        if b[i] in a:
            a.remove(b[i])
            cnt += 1

    return True if cnt == len(b) else False


for _ in range(t):
    a_s, b_s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()
    if a_s == b_s and is_same(a, b):
        print('=')
    elif a_s > b_s and is_part(a, b):
        print('>')
    elif a_s < b_s and is_part(b, a):
        print('<')
    else:
        print('?')

# a와 b 중 배열의 길이가 다르다
    # a가 크다 -> b는 a의 부분 ? -> >
    # b가 크다 -> a는 b의 부분 ? -> <
# 배열의 길이가 같다.
    # 내용이 같은가? -> =
# 모두 아니다. -> ?
