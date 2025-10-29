n = int(input())
arr = list(map(int, input().split()))

def isPrime(num):
    if num == 1: return 0

    for i in range(2, num + 1):
        if i * i > num: continue
        if num % i == 0: return 0

    return 1

cnt = 0
for a in arr:
    if isPrime(a): cnt += 1

print(cnt)
