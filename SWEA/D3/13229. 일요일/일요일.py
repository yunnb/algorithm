t = int(input())

days = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}

for t in range(1, t + 1):
    day = input()

    print(f'#{t} {days[day]}')
