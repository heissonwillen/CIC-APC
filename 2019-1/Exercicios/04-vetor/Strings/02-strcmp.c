#include <stdio.h>

void le_string(char* string){
	scanf("%1000[^\n]", string);
}

int tamanho(char* string){
	int i = 0;
	while(1){
		if (string[i] == '\0')
			return i;
		i++;
	}
	return 0;
}

int compara_tamanho(char* string_1, char* string_2){
	if (tamanho(string_1) < tamanho(string_2))
		return - 1;
	if (tamanho(string_1) > tamanho(string_2))
		return 1;
	return 0;
}

int main(){
	const int N = 1001;
	char string_1[N], string_2[N];

	le_string(string_1);
	getchar();
	le_string(string_2);

	printf("%d\n", compara_tamanho(string_1, string_2));

	return 0;
}