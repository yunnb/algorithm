n = int(input())

ans=[]

for i in range(1, n+1):
    num = str(i)
    cnt = num.count('3') + num.count('6') + num.count('9')

    if cnt == 0: ans.append(i)
    else: ans.append('-' * cnt)

print(*ans)
