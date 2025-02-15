seat = int(input())
seat_info = input()

holder = 1
for i in range(seat):
    if seat_info[i] == 'S':
        holder += 1
    elif seat_info[i] == 'L':
        holder += 0.5
if int(holder) > seat:
    holder = seat
    
print(int(holder))