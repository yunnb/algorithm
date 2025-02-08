#include <stdio.h>
#define pi 3.14159265359

int main(void)
{
	int r;
	double u, t;
	scanf("%d", &r);

	u = pi * r * r;
	t = 2 * r * r;

	printf("%.6lf\n", u);
    printf("%.6lf",t);
	return 0;
}