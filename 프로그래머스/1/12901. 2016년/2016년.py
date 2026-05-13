def solution(a, b):
    days = []
    dayOfWeek = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    for i in range(1, 13):
        if i == 2:
            days.append(29)
            continue

        d = 30 if i in (4, 6, 9, 11) else 31
        days.append(d)

    return dayOfWeek[(5 + (sum(days[:a - 1]) + b)) % 7 - 1]
