def solution(b, h, a):
    c_h = h
    cnt = 0 
    for i in range(a[len(a)-1][0] +1):
        if i == a[0][0]:  
            if c_h - a[0][1] > 0:
                c_h -= a[0][1]
                cnt = 0
                a.pop(0)
            else:
                return -1
        else:       
            cnt += 1
            c_h = min(c_h+b[1], h)
            if cnt == b[0]: 
                c_h = min(c_h+b[2], h)
                cnt = 0
    return c_h