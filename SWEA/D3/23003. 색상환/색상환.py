t = int(input())

colors = {'red': 1, 'orange': 2, 'yellow': 3, 'green': 4, 'blue': 5, 'purple': 6}
idx = [6, 1, 2, 3, 4, 5, 6, 1]

for _ in range(t):
    A, B = input().split(' ')
    a, b = colors[A], colors[B]

    if a == b:
        print('E')
    elif idx[a - 1] == b or idx[a + 1] == b:  # 인접한
        print('A')
    elif abs(a - b) == 3:  # 서로 반대인
        print('C')
    else:
        print('X')
