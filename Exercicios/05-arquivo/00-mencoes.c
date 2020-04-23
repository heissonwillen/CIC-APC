#include <stdio.h>
#include <stdlib.h>

void escreve(){
}

int cria_arquivo(char* nome_arquivo, int num_alunos){
	int i;
	char matricula[11];
	char mencao[3];

	FILE *fp = fopen(nome_arquivo, "w+");

	if (!fp){
		printf("Não foi possível abrir o arquivo.\n");
		return EXIT_FAILURE;
	}

	for (i = 0; i < num_alunos; i++){
		scanf("%s %s", matricula, mencao);
		fprintf(fp, "%s %s\n", matricula, mencao);

	}

	fclose(fp);
	return EXIT_SUCCESS;
}

int main(){
	char nome_arquivo[] = "mencoes.bin";
	int num_alunos;

	scanf("%d", &num_alunos);

	cria_arquivo(nome_arquivo, num_alunos);

	return 0;
}