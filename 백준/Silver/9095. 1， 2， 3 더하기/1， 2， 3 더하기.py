t = int(input())
li = [int(input()) for _ in range(t)]

dp = [1, 2, 4]
for i in range(3, max(li)):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for i in range(t):
    print(dp[li[i]-1])