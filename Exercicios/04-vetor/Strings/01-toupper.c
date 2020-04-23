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


void para_maiusculo(char* string){
	int i;
	for (i = 0; i < tamanho(string); i ++){
		if (string[i] >= 'a' && string[i] <= 'z')
			string[i] += ('A' - 'a');
	}
}

int main(){
	const int N = 1001;
	char string[N];

	le_string(string);
	para_maiusculo(string);

	printf("%s\n", string);

	return 0;
}