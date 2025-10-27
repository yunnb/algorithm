from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))

d = defaultdict(int)
for a in arr:
    d[str(a)] += 1

ans = 0
for k, v in d.items():
    if v > 1 :
        ans += (v * (v-1) // 2) * (n-v)

print(ans)

# 같은 수 두개 있는 것을 선택했을 때
# 또 다른수가 몇개인가 ?

# solved