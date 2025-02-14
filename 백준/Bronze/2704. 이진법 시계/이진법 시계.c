#include <stdio.h>
#include <math.h>

int main()
{
	int N, pow_n;
	int h, m, s;
	int tf_h[6], tf_m[6], tf_s[6];

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
	{
		scanf("%d:%d:%d", &h, &m, &s);

		for (int j = 0; j < 6; j++)
		{
			pow_n = pow(2, 5 - j);
			tf_h[j] = (h / pow_n) % 2;
			tf_m[j] = (m / pow_n) % 2;
			tf_s[j] = (s / pow_n) % 2;
		}
		
		// 3열 방식
		for (int j = 0; j < 6; j++) 
			printf("%d%d%d", tf_h[j], tf_m[j], tf_s[j]);
		printf(" ");
		
		// 3행 방식
		for (int j = 0; j < 6; j++)
			printf("%d", tf_h[j]);
		for (int j = 0; j < 6; j++)
			printf("%d", tf_m[j]);
		for (int j = 0; j < 6; j++)
			printf("%d", tf_s[j]);
		printf("\n");
	}
}