s = input()

a = s[0]
b = s[1]
if a == b:
    for w in s[2:]:
        if w != a: print(w)
else:
    if a == s[-1]: print(b)
    else: print(a)

# solved