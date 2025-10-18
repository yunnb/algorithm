Q = int(input())
stk = []
def check(stk):
    stack = []
    for s in stk:
        if s == '(':
            stack.append('(')
        else:
            if stack: stack.pop()
            else: return False
    return False if stack else True

for _ in range(Q):
    q = list(input().split())
    if q[0] == '1': stk.append(q[1])
    elif q[0] == '2': stk.pop()

    if check(stk): print('Yes')
    else: print('No')

# Time Limit