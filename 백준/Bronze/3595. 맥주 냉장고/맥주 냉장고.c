#include <stdio.h>

int main()
{
	int n;
	int min = 100000000;
	int a, b, c;
	int area;

	scanf("%d", &n);

	for (int i = 1; i <= n; i++)		
	{
		if (n % i == 0)					// n % i가 0이 되는 i 값만 가능
		{
			for (int j = 1; j <= n / i; j++)		// j는 1부터 n/i 까지 반복
			{
				if (n % (i * j) == 0)				// i와 j를 곱한 값을 n으로 나눈 나머지가 0이 되는 경우
				{
					for (int k = 1; k <= n / (i * j); k++)		// k는 1부터 n을 i*j로 나눈 몫까지 반복
					{
						// i * j * k는 n이 되어야 함
						if (i * j * k == n)
						{
							area = (i * j + j * k + i * k) * 2;		// 직육면체 겉넓이 구하는 공식

							// 겉넓이가 가장 작은 값을 min에 넣어주고 그때의 가로, 세로, 높이를 구함
							if (area < min)
							{
								min = area;
								a = i;
								b = j;
								c = k;
							}
						}
					}
				}
			}
		}
	}
	printf("%d %d %d", a, b, c);		// 가로, 세로, 높이 출력
}