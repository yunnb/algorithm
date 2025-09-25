n = int(input())

def print_m(n):
    if n == 0:
        return

    print_m(n-1)
    print("HelloWorld")

print_m(n)