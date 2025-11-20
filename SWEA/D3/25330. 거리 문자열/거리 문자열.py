from collections import defaultdict

t = int(input())

ans = []
for tc in range(1, t + 1):
    cnt = defaultdict(int)
    arr = list(map(int, input()))

    for a in arr:
        cnt[a] += 1

    chk = True
    for e in cnt:  # 개수확인하기
        if cnt[e] == 0 or cnt[e] == 2: continue
        chk = False
        break

    if not chk:
        ans.append('no')
        continue

    for i, a in enumerate(arr):
        if not chk: break

        cnt[a] += 1  # 첫 방문이면 3, 닫았다면 4
        if cnt[a] == 4: continue  # 닫았다면 나가기

        if i + a + 1 < len(arr):  # 다음 숫자가 전체 배열 범위 내인지 확인
            if arr[i + a + 1] != a:
                chk = False
        # 와야할 숫자의 위치가 배열 밖이라면
        else:
            chk = False

    ans.append('yes' if chk else 'no')

for a in ans:
    print(a)

# 각 숫자는 0부터 9까지 0개거나 두번 등장 . d 가 두번 등장한다면, 두 숫자 사이 개수는 d 개
# d[i+d[e]]
# 0 1 2 3 4 5
# 1 3 1 0 0 3
