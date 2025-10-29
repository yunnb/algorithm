m, n = map(int, input().split())

isPrimes = [ True for _ in range(n+1)] # 1-based
isPrimes[0], isPrimes[1] = False, False # 0, 1은 소수 x

# 가장 작은 소수부터 돌면서 소수의 배수들은 모두 False 처리
# 각 소수의 배수 체크 시작점은 i*i 부터 하면 됨 (이전 값들은 그전 소수로 인해 이미 확인 완료)
# 각 소수의 배수 체크 종료점은 i*i가 n보다 작거나 같을 때까지

for i in range(2, n+1): # 처리 안한 소수 찾기
    if not isPrimes[i]: continue # 합성수라면 패스
    for j in range(i*i, n+1, i): # 해당 소수의 배수 찾기
        isPrimes[j] = False


for i, p in enumerate(isPrimes[m:], start=m):
    if p: print(i)