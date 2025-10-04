n = int(input())

def print_m(s, e):
    if s <= e: return 
    print(s, end=' ')
    print_m(s-1, e)
    print(s, end=' ')
    

print_m(n, 0)