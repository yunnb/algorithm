from collections import defaultdict

n = list(map(int, input()))

d = defaultdict(int)

for e in n:
    d[e] += 1

for i in range(10):
    print(i, end=' ')

print()
for i in range(10):
    print(d[i], end=' ')
