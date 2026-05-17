def solution(k, m, score):
    ans = 0
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        if i+m > len(score):
            break

        ans += score[i+m-1] * m

    return ans


# 상자에 m개씩 포장 
# 한 상자 가격 = 가장 낮은 점수 * m 
# 최대 이익 계산 


# 4 3 -> 