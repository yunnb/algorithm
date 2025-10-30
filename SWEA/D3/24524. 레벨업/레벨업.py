t = int(input())

for _ in range(t):
    n = int(input())
    points = list(map(int, input().split()))

    # 완전 탐색
    min_cost = float('inf')
    for i in range(1, n - 1):  # 첫번째와 마지막은 무조건 방문
        cost = 0
        prev = 0
        for j in range(1, n):
            if i == j: continue
            cost += abs(points[j] - points[prev])
            prev = j

        min_cost = min(min_cost, cost)

    print(min_cost)