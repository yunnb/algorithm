t = int(input())

for tc in range(1, t + 1):
    arr = input()

    k = int(input())
    cmds = list(map(int, input().split()))

    for cmd in cmds:
        if cmd == 0: continue
        elif cmd > 0:
            i = cmd % len(arr)
            arr = arr[i:] + arr[:i]
        else:
            i = -cmd % len(arr)
            arr = arr[-i:] + arr[:-i]

    print(arr)
