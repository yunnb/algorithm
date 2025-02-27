try:
    while True:
        year = 0
        a = input().split(' ')

        n = float(a[0])
        b = float(a[1])
        m = float(a[2])

        while True:
            n = n*(1 + 0.01*b)
            year += 1
            if n > m:
                break
        print(year)
except:
    exit()