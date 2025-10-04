x, y = input().split()

version = {"Ocelot": 0, "Serval": 1, "Lynx":2}

if version[x] >= version[y]: print("Yes")
else: print("No")

# solved