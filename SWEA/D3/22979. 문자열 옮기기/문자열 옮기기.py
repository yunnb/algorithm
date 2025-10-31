t = int(input())

for _ in range(t):
    str = input()
    k = int(input())
    cmd = list(map(int, input().split()))

    idx = sum(cmd) % len(str)

    print(str[idx:] + str[:idx])
