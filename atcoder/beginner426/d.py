t = int(input())

# 문자열의 처음 또는 마지막 문자를 반전시켜 임의의 위치로 이동
# 0과 1로 각각 바꿨을 때 횟수 비교 하기 ?

# 01001
# 11001
# 10001
# 10000
# 00000

# 01101
# 11101
# 11001
# 10001
# 00001
# 00000

def to_zero(s):
    cnt = 0

    return cnt


def to_one(s):
    cnt = 0

    return cnt


for _ in range(t):
    n = int(input())
    s = list(map(int, input()))

    cnt0 = to_zero(s)
    cnt1 = to_one(s)

    print(min(cnt0, cnt1))
