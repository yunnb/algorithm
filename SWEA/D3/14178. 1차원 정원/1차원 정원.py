import math

t = int(input())

for t in range(1, t+1):
    n, d = map(int,input().split())

    ans = math.ceil(n / ((d*2) + 1))
    print(f'#{t} {ans}')