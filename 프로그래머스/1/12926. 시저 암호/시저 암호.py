def solution(s, n):
    ans = ''
    
    for e in s:
        if e == ' ':
            ans += e
            continue
            
        nxt = ord(e) + n 
        if 65 <= ord(e) <= 90:
            ans += chr(nxt) if nxt <= 90 else chr(nxt-26)

        if 97 <= ord(e) <= 122:
            ans += chr(nxt) if nxt <= 122 else chr(nxt-26)

    return ans