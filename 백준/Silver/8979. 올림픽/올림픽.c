#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int country;
	int gold[1000];
	int silver[1000];
	int bronze[1000];
	int grade = 1;
	int country_cnt, idx;

	scanf("%d %d", &country_cnt, &idx);
	--idx;
	for (int i = 0; i < country_cnt; ++i) {
		scanf("%d ", &country);
		scanf("%d %d %d", &gold[country - 1], &silver[country - 1], &bronze[country - 1]);
	}
	for (int i = 0; i < country_cnt; ++i) {
		if (gold[idx] < gold[i])
			++grade;
		else if (gold[idx] == gold[i]) {
			if (silver[idx] < silver[i])
				++grade;
			else if(silver[idx] == silver[i]) {
				if (bronze[idx] < bronze[i])
					++grade;
			}
		}
	}
	printf("%d", grade);

	return 0;
}