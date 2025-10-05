# 참가자가 짝수라면 반드시 모두 짝
# 참가자 n은 무조건 짝수 -> n/2 개의 쌍으로 나눠야 함
# 중복 짝 x
# 모든 쌍의 차이 중 최댓값이 가장 작도록
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    # 순서대로 짝 이루면 될듯 ?
    # 근데 차이값의 최대를 저장해야 함
    ans = 0
    for i in range(0, n-1, 2):
        ans = max(ans, abs(arr[i] - arr[i + 1]))

    print(ans)

# solved