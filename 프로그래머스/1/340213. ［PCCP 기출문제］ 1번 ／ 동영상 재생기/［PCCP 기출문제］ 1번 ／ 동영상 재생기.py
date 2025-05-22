def solution(video_len, pos, op_start, op_end, commands):
    vl = toSeconds(video_len)
    p = toSeconds(pos)
    os = toSeconds(op_start)
    oe = toSeconds(op_end)
    
    if p >= os and p<= oe:
        p = oe
    
    for c in commands:
        if c=="prev":
            p = p-10 if p - 10 >= 0 else 0

        elif c=="next":
            p = p+10 if p + 10 <= vl else vl 

        if p >= os and p< oe:
            p = oe

    return toMinute(p)

def toSeconds(time):
    time = time.split(':')
    time = int(time[0])*60 + int(time[1]) 
    return time

def toMinute(time):
    mm = "{:02}".format(int(time / 60))
    ss = "{:02}".format(time % 60)
    return mm + ":" + ss 
