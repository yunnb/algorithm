n, q = map(int, input().split())

pcs = []
for i in range(1, n+1):
    pcs.append(i)

for _ in range(q):
    x, y = map(int, input().split())
    cnt = 0
    for i, pc in enumerate(pcs):
        if pc <= x:
            pcs[i] = y
            cnt += 1
    print(cnt)


# time limited TT