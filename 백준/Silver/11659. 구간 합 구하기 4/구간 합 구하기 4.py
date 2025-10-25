n, m = map(int, input().split())

nums = list(map(int, input().split()))
dp = [0] * (n + 1)  # 1-based

for i, n in enumerate(nums):
    dp[i + 1] = dp[i] + n

for _ in range(m):
    i, j = map(int, input().split())

    if i == 1:
        print(dp[j])
    else:
        print(dp[j] - dp[i - 1])
