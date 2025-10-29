n = int(input())

f = 1
for i in range(1, n + 1):
    f *= i

arr = list(str(f))
arr.reverse()

cnt = 0
for a in arr:
    if a == '0': cnt += 1
    if a != '0': break

print(cnt)
