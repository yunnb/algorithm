t = int(input())

for _ in range(t):
    cmd = list(input())

    ans = 0
    for i in range(2):
        cur_pos = [0] * len(cmd)

        if cmd[0] == 'L' or (cmd[0] == '?' and i == 0):
            cur_pos[0] = -1
        elif cmd[0] == 'R' or (cmd[0] == '?' and i == 1):
            cur_pos[0] = +1

        max_dist = 1
        
        for j, c in enumerate(cmd[1:], start=1):
            if c == 'L' or (c == '?' and i == 0):
                cur_pos[j] = cur_pos[j - 1] - 1
            elif c == 'R' or (c == '?' and i == 1):
                cur_pos[j] = cur_pos[j - 1] + 1
            max_dist = max(max_dist, abs(cur_pos[j]))

        ans = max(ans, max_dist)

    print(ans)