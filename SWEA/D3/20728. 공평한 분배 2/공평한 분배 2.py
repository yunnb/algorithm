t = int(input())

for t in range(1, t + 1):
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    candies.sort()
    ans = candies[n - 1] - candies[0]
    
    for i in range(n - k + 1):
        ans = min(ans, candies[i + k - 1] - candies[i])

    print(f'#{t} {ans}')
