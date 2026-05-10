def solution(arr, commands):
    ans = []
    for cmd in commands:
        a = arr[cmd[0]-1:cmd[1]]
        a.sort()
        ans.append(a[cmd[2]-1])

    return ans