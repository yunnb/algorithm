#include <stdio.h>
int main(void)
{
	long long int s, sum = 0, max = 0;
	scanf("%lld", &s);

	for (int i = 1; sum <= s; i++)
	{
		sum += i;
		max++;
	}
    printf("%d", max-1);
}
