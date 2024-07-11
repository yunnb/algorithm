#include <stdio.h>

int main()
{
    int n, m;
    // limit_speed[x]는 시작 지점에서 x km 떨어진 지점에서의 제한 속도
    // mySpeed[x]는 시작 지점에서 x km 떨어진 지점에서의 연정이의 속도
    int limit_speed[100] = { 0 };
    int mySpeed[100] = { 0 };
    int lastIdx = 0;
    int len, speed;
    int max = 0;

    scanf("%d %d", &n, &m);             // n개의 구간, 연정이가 달린 m개의 구간

    // 각 구간의 길이와 제한 속도
    for (int i = 0; i < n; i++)         // n번 반복
    {
        scanf("%d %d", &len, &speed);   // 각 구간의 길이와 제한속도 입력

        for (int j = lastIdx; j < lastIdx + len; j++)
            limit_speed[j] = speed;
        lastIdx += len;
    }
    lastIdx = 0;

    // 연정이가 달린 각 구간의 길이와 해당 구간에서 달린 속도
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &len, &speed);

        for (int j = lastIdx; j < lastIdx + len; j++)
            mySpeed[j] = speed;
        lastIdx += len;
    }

    // 1 ~ 100까지 반복문을 돌며, 두 속도를 비교하여 가장 큰 값 출력
    for (int i = 0; i < 100; i++)
    {
        int diff = mySpeed[i] - limit_speed[i];

        if (diff > max)
            max = diff;
    }

    printf("%d", max);      // 속도 위반한 최댓값
}