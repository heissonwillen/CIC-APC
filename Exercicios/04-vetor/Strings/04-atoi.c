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


int char_para_inteiro(char c){
	return c - '0';
}

int string_para_inteiro(char* string){
	int n = 0, ordem = 1, i = (tamanho(string) - 1);

	while (string[i] != ' '){
		n += char_para_inteiro(string[i]) * ordem;
		string[i] = '\0';
		ordem *= 10;
		i--;
	}
	return n;
}

int main(){
	const int N = 1001;
	char string[N];

	le_string(string);
	printf("%d\n", string_para_inteiro(string)); 
	printf("%d\n", string_para_inteiro(string)); 
	return 0;
}