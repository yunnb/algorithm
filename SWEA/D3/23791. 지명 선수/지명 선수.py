from collections import deque

t = int(input())


def select(team, G, players):
    cand = G.popleft()
    if players[cand] == '-':  # 안뽑힘
        players[cand] = team
        return players
    else:
        return select(team, G, players)


for _ in range(t):
    n = int(input())
    A = deque(map(int, input().split()))
    B = deque(map(int, input().split()))

    players = ['-'] * (n + 1)  # 1-based

    for i in range(1, n + 1):
        if i % 2 != 0:  # 홀수라면 A 차례
            players = select('A', A, players)
        else:  # 짝수라면 B 차례
            players = select('B', B, players)

    print(*players[1:], sep='')