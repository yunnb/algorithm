testcase = int(input())

for i in range(testcase):
    message = input()
    s = int(len(message)**(1/2))

    o_message =''
    for j in range(s-1, -1, -1):
        for i in range(0, len(message), s):
            unt = message[i:i+s]
            o_message += unt[j]
    print(o_message)