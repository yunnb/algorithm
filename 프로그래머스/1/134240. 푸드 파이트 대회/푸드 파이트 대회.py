def solution(food):
    arr = []

    for i, f in enumerate(food[1:], start=1):
        for _ in range(f//2):
            arr.append(str(i))

    return ''.join(arr) + '0' + ''.join(arr[::-1])