import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
result = True

for i in range(M):
    n = int(input())
    book = list(map(int, input().split()))
    for j in range(n-1):
        if book[j] < book[j+1]:
            result = False
            break

if result:
    print('Yes')
else:
    print('No')