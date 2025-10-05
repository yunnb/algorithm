t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    zero = 0
    minusone = 0
    for a in arr:
        if a == 0: zero += 1
        elif a == -1: minusone += 1

    cnt = zero
    if minusone % 2 != 0: cnt += 2

    print(cnt)
    # 0 을 없애야하고
    # -1 이 짝수개 있어야함
    # 0은 무조건 바꿔야함 ! -> 0 에서 무조건 1 증가 해야하니까 0개수만ㅌ큼 카운트
    # -1 이 홀수라면 두번 플러ㅡ

# solved