n = int(input())

times = list(map(int, input().split()))
times.sort()

ans, prev = 0, 0
for i in range(n):
    prev += times[i]
    ans += prev

print(ans)