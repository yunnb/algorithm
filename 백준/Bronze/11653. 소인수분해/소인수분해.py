n = int(input())
arr = []
# n을 i로(2부터) 나눠질때까지 계속 나눔
# 나눠진다면 소인수 목록에 추가
# 안나눠진다면 i+1

for i in range(2, n + 1):
    if i * i > n: break # 속도 비교! 

    if n % i == 0:
        while n % i == 0:
            print(i)
            n //= i

if n != 1: print(n)