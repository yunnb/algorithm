#include <stdio.h>
#include <math.h>

int main() {
	int n;
	int m;
	int P[2000];
	int Q[2];
	long long int result = 0;

	scanf("%d %d", &n, &m);
	
	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &P[i*2], &P[i*2 + 1]);
	}

	for (int i = 0; i < m; ++i) {
		scanf("%d %d", &Q[0], &Q[1]);
		for (int i = 0; i < n; ++i) {
			if (pow(Q[0] - P[i * 2], 2) + pow(Q[1] - P[i * 2 + 1], 2) > result)
				result = pow(Q[0] - P[i * 2], 2) + pow(Q[1] - P[i * 2 + 1], 2);
		}
	}

	printf("%lld", result);

	return 0;
}