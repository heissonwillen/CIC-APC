/*
Aluno:			Heisson Willen Esteves Lima
Matrícula		190014181
Disciplina:		Algoritmos e Programação de Computadores
Data:			24/06/2019

Descrição:		Recebe como argumento da função main o nome de um arquivo
 				binário e lê deste arquivo uma quantidade indeterminada de
 				registros do tipo mensagem_secreta.
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int segredo;
	char mensagem[101];
} __attribute__ ((packed)) mensagem_secreta;

int tamanho_da(char* string){
	int i = 0;
	while (string[i] != '\0')
		i++;
	return i;
}

mensagem_secreta decifra(mensagem_secreta msg){
	int i, tamanho = tamanho_da(msg.mensagem); 
	char c;

	for (i = 0; i < tamanho; i++){
		c = msg.mensagem[i];

		if (((c <= 'Z') && (c - msg.segredo < 'A') && (c >= 'A')) || ((c <= 'z') && (c - msg.segredo < 'a') && (c >= 'a')))
			c += 26;
		if (c != '\n')
			msg.mensagem[i] = c - msg.segredo;
	}
	return msg;
}

int cria_novo_arquivo(char* arquivo){
	char backup[500];
	int contador = 0;

	mensagem_secreta msg;

	FILE *saida = NULL;
	FILE *entrada = fopen(arquivo, "rb+");

 	if(!entrada) {
		printf("Erro! Não foi possível abrir o arquivo.");
		fclose(entrada);
		return EXIT_FAILURE;
	}

	while (1){
		sprintf(backup, "%s-%d.txt", arquivo, contador);
	 	saida = fopen(backup, "w+");

		fread(&msg.segredo, sizeof(msg.segredo), 1, entrada);
		fread(msg.mensagem, sizeof(msg.mensagem), 1, entrada);

		if (feof(entrada))
			break;

		msg = decifra(msg);
		printf("%s\n", msg.mensagem);
		fprintf(saida, "%s\n", msg.mensagem);

		contador++;
	}

	fclose(entrada);
	fclose(saida);
	return EXIT_SUCCESS;
}

int main(int argc, char **argv) {
	if (argc != 2){
		printf("Erro! Não foi possível identificar o arquivo.\n");
		return 0;
	}

	printf("Nome do arquivo: %s\n", argv[1]);

	cria_novo_arquivo(argv[1]);
    return 0;
}
