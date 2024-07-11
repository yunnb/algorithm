N = int(input())
N_list = [1, 1]
for i in range (2, N):
		N_list.append(N_list[i-2] + N_list[i-1])
r = N_list[N-2]+N_list[N-1]*2
if N == 1:
    print(4)
else:
    print(r*2)