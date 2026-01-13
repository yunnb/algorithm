def schedule(t):
    h = t // 100
    m = t % 100

    m += 10
    if m >= 60:
        h += 1
        m -= 60

    return h * 100 + m

def solution(schedules, timelogs, startday):
    l = len(schedules)
    late = [False for _ in range(l)]
    
    for i in range(l):
        if late[i]: continue
            
        for nday, timelog in enumerate(timelogs[i]):
            if late[i]: continue

            day = (nday+startday-1) % 7 + 1
            if day == 6 or day == 7: 
                continue
            if timelog > schedule(schedules[i]): 
                late[i] = True
            
    ans = 0
    for l in late:
        if not l: ans += 1
        
    return ans