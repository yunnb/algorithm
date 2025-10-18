from collections import defaultdict
n, k = map(int, input().split())
s = list(input())

dic = defaultdict(int)
for i, e in enumerate(s[:len(s)-k+1]):
    dic[''.join(s[i:i+k])] += 1

ans = []
keys = list(dic.keys())
values = list(dic.values())
for i in range(len(keys)):
    if values[i] == max(values):
        ans.append(keys[i])

ans.sort()
print(max(values))
print(*ans)

# solved