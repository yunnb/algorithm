t = int(input())

for _ in range(t):
    n = int(input())
    matrix = [list(map(int,input().split())) for _ in range(n)]

    arr = []
    cnt = 0
    for i, m in enumerate(matrix[0], start=1):
        if i == m: arr.append(True)
        else: arr.append(False)

    for i in range(n-1, -1, -1):
        if arr[i]: continue

        cnt +=1
        for j in range(1, i+1):
            if arr[j]: arr[j] = False
            else: arr[j] = True

    print(cnt)