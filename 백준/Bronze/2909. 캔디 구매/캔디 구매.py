c, k = map(int, input().split())

if len(str(c)) == k:
    print(pow(10, k))
else:
    print(round(c, -k))