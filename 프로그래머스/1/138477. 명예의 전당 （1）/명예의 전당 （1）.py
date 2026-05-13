def solution(k, score):
    ans = []
    arr = []

    for s in score:
        arr.append(s)
        arr.sort(reverse=True)

        if len(arr) >= k:
            ans.append(arr[k-1])
        else:
            ans.append(arr[-1])

    return ans
