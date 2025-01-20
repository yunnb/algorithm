#include <stdio.h>

int main() {
	int len;
	char ch[30];
	
	scanf("%d", &len);
	scanf("%s", ch);
	
	if(ch[len - 1] == 'r' || ch[len - 1] == 's' || ch[len - 1] == 'e' || ch[len - 1] == 'f' || ch[len - 1] == 'a' || ch[len - 1] == 'q' || ch[len - 1] == 't' || ch[len - 1] == 'd' || ch[len - 1] == 'w' || ch[len - 1] == 'c' || ch[len - 1] == 'z' || ch[len - 1] == 'x' || ch[len - 1] == 'v' || ch[len - 1] == 'g')
		printf("1");
	else
		printf("0");
}