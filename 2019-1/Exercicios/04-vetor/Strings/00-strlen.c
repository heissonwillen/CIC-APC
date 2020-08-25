#include <stdio.h>

int tamanho(char* string){
	int i = 0;

	while(1){
		if (string[i] == '\0'){
			return i;
		}
		i++;
	}

	return i;
}

int main(){
	const int N = 1001;
	char string[N];

	scanf("%1000[^\n]", string);
	printf("%d\n", tamanho(string));

	return 0;
}