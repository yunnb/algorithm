n = int(input())

def print_asc(n):
    if n == 0: return
    print_asc(n-1)
    print(n, end=' ')


def print_desc(n):
    if n == 0: return 
    print(n, end=' ')
    print_desc(n-1)

print_asc(n)
print()
print_desc(n)
