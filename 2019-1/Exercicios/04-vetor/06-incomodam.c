#include <stdio.h>

int le_num_valentoes(){
	int num_valentoes;
	scanf("%d", &num_valentoes);
	return num_valentoes;
}

int preenche_vetor(char* vetor){
	char c;
	int i = 0;

	getchar();
	
	while (1) {
		c = getchar();
		if (c == '\n')
			return i;
  		vetor[i] = c;
		i++;
	}
	return i;
}

void mostra_vetor(char* vetor, int n){
	int i;
	for (i = 0; i < n; i++){
		printf("%c", vetor[i]);
	}
}

void vinganca_do_elefante(char* vetor, int num_valentoes, int n){
	int i, j;

	for (i = 1; i <= num_valentoes; i++){
		printf("%d ", i);
		mostra_vetor(vetor, n);

		if (i == 1)
			printf(" incomoda muita gente...\n");
		else
			printf("s incomodam muita gente...\n");

		printf("%d ", i + 1);
		mostra_vetor(vetor, n);
		printf("s ");

		for (j = 0; j <= i; j++){
			printf("incomodam");
			if (j < i)
				printf(", ");
			else
				printf(" ");
		}

		printf("muito mais.\n");
	}
}

int main(){
	const int N = 50;
	char vetor[N];
	int num_valentoes;

	/*scanf("%d", &num_valentoes);*/

	int num_valentoes = le_num_valentoes();
	int n = preenche_vetor(vetor);
	vinganca_do_elefante(vetor, num_valentoes, n);

	return 0;
}