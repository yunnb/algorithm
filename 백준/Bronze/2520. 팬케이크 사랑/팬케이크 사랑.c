#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int test_case, min, num;
	int material[5] = {0};
	int topping[4] = {0};
	int need[9] = {8, 8, 4, 1, 9, 1, 30, 25, 10};

	scanf("%d", &test_case);
	for (int i = 0; i < test_case; i++) {
		scanf("%d %d %d %d %d", &material[0], &material[1], &material[2], &material[3], &material[4]);
		scanf("%d %d %d %d", &topping[0], &topping[1], &topping[2], &topping[3]);
		min = (int)((double)material[0] / need[0] * 16);
		for (int j = 1; j < 5; j++) {
			num = (int)((double)material[j] / need[j] * 16);
			if (num < min)
				min = num;
		}
		num = 0;
		for (int j = 0; j < 4; j++) {
			num += topping[j] / need[j + 5];
		}
		if (num < min)
			min = num;
		printf("%d\n", min);
	}
	return 0;
}