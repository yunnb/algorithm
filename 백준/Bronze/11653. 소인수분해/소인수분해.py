n = int(input())
arr = []
# n을 i로(2부터) 나눠질때까지 계속 나눔
# 나눠진다면 소인수 목록에 추가
# 안나눠진다면 i+1

for i in range(2, n+1):
    if n == 1: break

    if n % i == 0: # 나누어 떨어진다면
        while n >= 1:
            if n % i != 0: break
            n //= i
            arr.append(i)

print(*arr, sep='\n')