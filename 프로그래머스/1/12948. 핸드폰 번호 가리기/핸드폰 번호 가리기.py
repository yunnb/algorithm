def solution(phone):
    cnt = len(phone)-4
    return cnt * '*' + phone[cnt:]  
