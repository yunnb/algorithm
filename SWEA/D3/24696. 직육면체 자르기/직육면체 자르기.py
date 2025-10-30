t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    print(1 if (a * b * c) % 2 == 0 else 2)