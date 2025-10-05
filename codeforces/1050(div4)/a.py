t = int(input())

def sum(x, n):
    if n % 2 == 0:  print(0)
    else: print(x)

for i in range(t):
    x, n = map(int, input().split())
    sum(x, n)