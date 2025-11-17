import math

FALSE = 'Broken'
TRUE = 'Possible'

t = int(input())

ans = []
for tc in range(1, t + 1):
    n, pd, pg = map(int, input().split())

    if n == 0 and pd > 0: # 오늘 한 판도 안했는데 승률이 있다면
        ans.append(FALSE)
        continue

    # 한 판이라도 졌다면, 승률 100은 안됨
    if pd != 100 and pg == 100:
        ans.append(FALSE)
        continue

    # 한 판이라도 이겼다면 ,승률 0은 안됨
    if pd > 0 and pg == 0:
        ans.append(FALSE)
        continue

    chk = False
    for i in range(1, n+1):  # d * pd 가 정수가 되어야 함
        if math.ceil(i * pd/100) == math.floor(i * pd/100):
            chk = True
            break

    if chk: ans.append(TRUE)
    else: ans.append(FALSE)


for tc, a in enumerate(ans, start=1):
    print(f'#{tc} {a}')
