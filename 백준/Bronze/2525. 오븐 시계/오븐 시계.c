#include <stdio.h>

int main(void)
{
	int A, B, C;
	scanf("%d %d %d", &A, &B, &C);
	if ((B + C) % 60 == 0)
	{
		if (A + (B + C) / 60 < 24)
		{
			printf("%d %d", (A + (B + C) / 60), 0);
		}

		else if (A + (B + C) / 60 >= 24)
		{
			printf("%d %d", (A + (B + C) / 60) % 24, 0);
		}
	}

	else
	{
		if (A + ((B + C) / 60) >= 24)
		{
			printf("%d %d", (A + (B + C) / 60) % 24, (B + C) % 60);
		}

		else
		{
			if (B + C >= 60)
			{
				printf("%d %d", (A + (B + C) / 60), (B + C) % 60);
			}
			else
			{
				printf("%d %d", A, B + C);
			}
		}


	}

	
	return 0;
}
