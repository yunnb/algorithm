t = int(input())

for _ in range(t):
    b, w, x, y, z = map(int, input().split())

    basic = (b * x) + (w * y)
    if b == w:
        print(max(basic, b * 2 * z))
    else:
        bigger, smaller = max(b, w), min(b, w)
        bigger_point = x if b > w else y
        switch = (smaller * 2 * z) + ((bigger - smaller) * bigger_point)

        print(max(basic, switch))