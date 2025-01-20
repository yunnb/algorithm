#include <stdio.h>

int main() {
	int N, i, arr[32], arr_2[32], cnt = 0, result = 0;
	
	scanf("%d", &N);
	
	for (i = 0; ; i++) {		
		if (N % 2 == 0) {
			arr[i] = 0;
			arr_2[i] = 1;
		}
		else {
			arr[i] = 1;
			arr_2[i] = 0;
		}
		cnt++;
		if (N == 1) break;
		N =  N / 2;
	}
	
	for (i = 31; i >= cnt; i--) {
		arr[i] = 0;
		arr_2[i] = 1;
	}
	
	arr_2[0]++;
	for (i = 0; i < cnt; i++)
		if (arr_2[i] == 2) {
			arr_2[i] = 0;
			arr_2[i + 1]++;
		}
	
	for (i = 0; i < 32; i++) if (arr[i] != arr_2[i]) result++;
	
	printf("%d", result);
	
}