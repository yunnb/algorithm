n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = False
for i in range(n):
    res = sum(arr[:i]) + sum(arr[i+1:])
    if res == m: ans = True

print('Yes') if ans else print('No')

# solved