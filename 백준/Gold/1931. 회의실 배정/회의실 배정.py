n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end = arr[0][1] # 이전 회의 종료 시간
for s, e in arr[1:]:
    if end <= s:
        cnt += 1
        end = e

print(cnt)