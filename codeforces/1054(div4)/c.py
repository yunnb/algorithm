# 길이 n의 배열 a, 정수 k
# 한번의 연산 -> a[i]를 0~n 사이의 값으로 바꾸기
# mex(a) = k -> 배열에 존재 하지 않는 가장 작은 비음수 정수

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = [0] * (n+1)
    for a in arr:
        cnt[a] += 1

    ans = 0
    for i, c in enumerate(cnt):
        # k보다 작은 수가 무조건 하나 이상
        if i < k and c < 1: ans += 1

    print(max(ans, cnt[k]))

# solved