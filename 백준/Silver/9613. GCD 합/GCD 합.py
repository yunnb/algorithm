import math

t = int(input())
for _ in range(t):
    cmd = list(map(int, input().split()))
    n, arr = cmd[0], cmd[1:]

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans += math.gcd(arr[i], arr[j])
    
    print(ans)
