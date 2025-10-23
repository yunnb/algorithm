n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

dp = [r[:] for r in costs]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
print(min(dp[-1]))