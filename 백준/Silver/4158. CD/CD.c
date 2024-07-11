#include <stdio.h>
#include <stdlib.h>

int answer;

void binsearch(int *Ma, int n, int key) {
    int low = 0, high = n - 1, mid;
    
    while (low <= high) {
        mid = (low + high) / 2;
        if (key == Ma[mid]) {
            answer++;
            break;
        }
        else if (key < Ma[mid]) high = mid - 1;
        else if (key > Ma[mid]) low = mid + 1;
    }
}

int main() {
	while(1) {
		answer = 0;
		int N, M, i;
		int *Na, *Ma;
		scanf("%d %d", &N, &M);
		
		if (N == 0 && M == 0) break;
		
		Na = (int*)malloc(sizeof(int) * N);
		Ma = (int*)malloc(sizeof(int) * M);
	
		for (i = 0; i < N; i++) scanf("%d", &Na[i]);
		for (i = 0; i < M; i++) scanf("%d", &Ma[i]);
	  for (i = 0; i < N; i++) binsearch(Ma, M, Na[i]);
		
		free(Na);
		free(Ma);
		printf("%d\n", answer);
	}
}