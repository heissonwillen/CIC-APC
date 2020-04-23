/**      @file: conway.c
 *     @author: Guilherme N. Ramos (gnramos@unb.br)
 * @disciplina: Algoritmos e Programação de Computadores
 *
 * Implementação do "Jogo da Vida" de Conway, complete o código das funções
 *  - blinker
 *  - glider
 *  - aleatorio
 *  - atualiza
 *  - quantos_ciclos
 *  - exibe
 *  - atualiza */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/* Poucas linhas de modo que "caiba na tela"... Quando todo o código estiver
 * pronto, tente com dimensões maiores. */
#define LINHAS 20
#define COLUNAS 50

#define VIVO '*'
#define MORTO ' '

typedef char status;
typedef status campo[LINHAS][COLUNAS];

/* Você pode ver os padrões no seguinte link:
   https://pt.wikipedia.org/wiki/Jogo_da_vida#Exemplos_de_imagens */


/* Inicializa com o padrão "blinker". É um padrão simples, em alguma coordenada,
defina 3 posições contíguas como VIVO. Ex:

   *
   *
   *

*/
void blinker(campo m) {

}

/* Inicializa com o padrão "glider". É um padrão simples, em alguma coordenada,
defina 5 posições como VIVO de acordo com o padrão abaixo (
https://pt.wikipedia.org/wiki/Jogo_da_vida#Exemplos_de_imagens). Ex:

   ***
   *
    *


*/
void glider(campo m) {

}

/* Inicializa o campo, definindo o status de cada uma das células como VIVO ou
MORTO com 50% de chance. */
void aleatorio(campo m) {

}


/* Inicializa o campo. */
void inicializa(campo m) {
	/* Define todas as células do campo como MORTO. */

	switch(rand()%3) { /* Aleatoriamente, escolhe um das 3 opções */
		case 0:
			blinker(m);
			break;
		case 1:
			glider(m);
			break;
		default:
			aleatorio(m);
	}
}

/* Lê do usuário um número inteiro que indica a quantidade de ciclos a serem
simulados. Retorna apenas quando o valor for inteiro e positivo. */
int quantos_ciclos() {

}


/* Escreve o campo na saída padrão. */
void exibe(campo m) {
	/* Mostra o campo como uma "matriz" bidimensional. */
}

/* Atualiza o campo conforme as regras do jogo:
 *
 * 1) Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
 * 2) Qualquer célula viva com mais de três vizinhos vivos morre de
 * superpopulação.
 * 3) Qualquer célula morta com exatamente três vizinhos vivos se torna uma
 * célula viva.
 * 4) Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo
 * estado para a próxima geração. */
void atualiza(campo m) {
	/* Atenção, uma célula que esteja na borda do campo não possui vizinho(s)
	 * além da borda. Por exemplo, uma célula de canto tem apenas os 3 vizinhos
	 * "para dentro" do campo. */
}

/* Realiza alguma ação para aguardar a próxima atualização. */
void aguarda_a_atualizacao() {
	printf("\n\nPressione [Enter] para continuar.");
	getchar();
	/* Isso poderia (deveria) ser alterado para uma ação automática... */
}

/* Laço principal de execução. */
int main() {
	/* NÃO ALTERE AS INSTRUÇÕES A PARTIR DAQUI */

	int i, ciclos;
	campo jogo_da_vida;

	srand(time(NULL)); /* Inicialização de números "aleatórios". */
	inicializa(jogo_da_vida);

	ciclos = quantos_ciclos();

	for(i = 1; i <= ciclos; ++i) {
		system("clear"); /* Muito cuidado com este tipo de instrução... */

		printf("Ciclo %d:\n", i);

		exibe(jogo_da_vida);
		aguarda_a_atualizacao();
		atualiza(jogo_da_vida);
	}

    return 0;
}