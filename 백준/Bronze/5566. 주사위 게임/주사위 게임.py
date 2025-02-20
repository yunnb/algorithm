N, M = map(int, input().split(' '))
sg = 1
cnt = 0
ins_list = []
dice_list = []

for i in range(N):
    instruction = int(input())
    ins_list.append(instruction)

for j in range (M):
    dice = int(input())
    dice_list.append(dice)

for j in range(M):
    
    cnt += 1
    d = sg
    sg += dice_list[j] 
    if sg >= N:
        print(cnt)
        exit()
    sg += ins_list[d+dice_list[j]-1]
    if sg >= N:
        print(cnt)
        exit()
