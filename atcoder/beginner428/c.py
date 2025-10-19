# Q = int(input())
# stk = []
# def check(stk):
#     stack = []
#     for s in stk:
#         if s == '(':
#             stack.append('(')
#         else:
#             if stack: stack.pop()
#             else: return False
#     return False if stack else True
#
# for _ in range(Q):
#     q = list(input().split())
#     if q[0] == '1': stk.append(q[1])
#     elif q[0] == '2': stk.pop()
#
#     if check(stk): print('Yes')
#     else: print('No')

# Time Limit

# ----------------
# 여는 괄호 1, 닫는 괄호 -1 이라 할 때,
# 합이 음수가 된 적이 있다면 No
# 끝났을 때 합이 0이면 Yes

q = int(input())
a = [0] # 높이 기록 (pop 사용 시 되돌아가야하므로 배열로 관리)
b = [0] # 지금까지 최저 높이 기록
for i in range(q):
    cmd = input().split()
    if cmd[0] == '1':
        v = 1 if cmd[1] == '(' else -1
        a.append(a[-1] + v)
        b.append(min(b[-1], a[-1]))
    else:
        a.pop()
        b.pop()

    if a[-1] == 0 and b[-1] == 0: print('Yes')
    else: print('No')