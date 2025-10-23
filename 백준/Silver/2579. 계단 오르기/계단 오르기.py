t = int(input())
s = [int(input()) for _ in range(t)]

if t == 1:
    print(s[0])
    exit()
if t == 2:
    print(s[0] + s[1])
    exit()

dp = [0] * t
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[0], s[1]) + s[2]

for i in range(3, t):
    dp[i] = max(dp[i - 2], dp[i - 3] + s[i - 1]) + s[i]

print(dp[t - 1])
