import math

t = int(input())

for t in range(1, t + 1):
    a, b = input().split()
    if a == b:
        print(f"#{t} {'yes'}")
        continue

    al, bl = len(a), len(b)
    l = al * bl // math.gcd(al, bl)
    ans = 'yes' if a * (l // al) == b * (l // bl) else 'no'

    print(f"#{t} {ans}")
