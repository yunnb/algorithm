t = int(input())

for tc in range(1, t + 1):
    NUM = input()
    num = int(NUM)
    n = len(NUM)

    min_ans, max_ans = num, num

    for i in range(n):
        for j in range(i + 1, n):
            cand = list(NUM)
            cand[i], cand[j] = cand[j], cand[i]

            if cand[0] == '0': continue

            cand = int(''.join(cand))
            min_ans = min(min_ans, cand)
            max_ans = max(max_ans, cand)

    print(f'#{tc} {min_ans} {max_ans}')
