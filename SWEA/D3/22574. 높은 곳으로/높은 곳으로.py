t = int(input())

for _ in range(t):
    n, p = map(int, input().split())

    floor = 0
    need_stop = False
    for i in range(1, n + 1):
        if floor + i == p:
            need_stop = True

        floor += i

    print(floor if not need_stop else floor - 1)

# 지금 건널건지
# 한번 참고 건널건지 
# 멈춰야하는 상황이 생긴다면, 1번째에서 멈추고 나머지는 쭉쭉 가면 되지 않나?
