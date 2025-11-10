t = int(input())

ans = []
for _ in range(t):
    a, b = map(int, input().split())

    if a == b:
        ans.append(0)
        continue
    elif a > b:
        ans.append(-1)
        continue

    cha = b - a
    if cha == 1:
        ans.append(-1)
        continue

    ans.append(cha // 2)

for t, a in enumerate(ans, start=1):
    print(f'#{t} {a}')

# 2로 나눈 몫만큼 +1
# 2로 나눈 후 나머지가 0 이 아니라면
# -1 +1 (2로 연산한 횟수 1 빼고, 3으로 연산)
