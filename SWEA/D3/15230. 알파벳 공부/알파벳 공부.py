t = int(input())

answer = 'abcdefghijklmnopqrstuvwxyz'
for t in range(1, t + 1):
    string = input()

    ans = 0
    for a, s in zip(answer, string):
        if a == s: ans += 1
        else: break

    print(f'#{t} {ans}')
