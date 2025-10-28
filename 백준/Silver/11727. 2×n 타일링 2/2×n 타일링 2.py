n = int(input())

if n == 1:
    print(1)
    exit(0)
if n == 2:
    print(3)
    exit(0)

dp = [0, 1, 3] # 1-based

for i in range(3, n+1):
    dp.append((dp[i-1] + (dp[i-2]*2))%10007)

print(dp[-1])