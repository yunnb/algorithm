n = int(input())

line = 1
g = 0

while True:
    g += line
    if g<n:
        line+=1
    else:
        g -= line
        index = n - g
        
        if (line % 2 == 0):
            print(index, "/", line + 1 - index, sep='')
            break
        else:
            print(line + 1 - index, "/", index, sep='')
            break

