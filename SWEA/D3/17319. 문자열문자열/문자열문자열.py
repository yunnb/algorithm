t = int(input())

for t in range(1, t + 1):
    a = int(input())
    string = input()

    if a % 2 == 0 and string[:a // 2] == string[a // 2:]: ans = 'Yes'
    else: ans = 'No'

    print(f'#{t} {ans}')
