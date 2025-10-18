while True:
    stack = []
    text = input()
    if text == '.': break;

    # 여는 괄호면 stack
    # 닫는 괄호면
        # 짝이 맞으면 pop
        # 짝이 안맞으면 no 출력 후 다음거
    # 스택이 남아있으면 no 출력

    isBalanced = True

    for t in text:
        if isBalanced:
            if t == '(' or t == '[': # 여는 괄호면 stack
                stack.append(t)
            
            elif t == ')': # 닫는 괄호면 1
                if len(stack) == 0: 
                    isBalanced = False
                elif stack[-1] == '(': # 짝이 맞으면 pop
                    stack.pop()
                else: isBalanced = False # 안 맞으면 no
            elif t == ']': # 닫는 괄호면 2
                if len(stack) == 0 : 
                    isBalanced = False
                elif stack[-1] == '[': # 짝이 맞으면 pop
                    stack.pop()
                else: isBalanced = False 
            else: continue 

    if len(stack) > 0: isBalanced = False

    if isBalanced: print('yes')
    else: print('no')