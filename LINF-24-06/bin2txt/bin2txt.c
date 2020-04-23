/**      @file: bin2txt.c
 *     @author: Guilherme N. Ramos (gnramos@unb.br)
 * @disciplina: Algoritmos e Programação de Computadores
 *
 * Mensagens secretas são mais interessantes que as outras, principalmente em
 * tempos de tanta insegurança... Atualmente, a solução para comunicação segura
 * é escrever uma mensagem, cifrá-la e enviá-la. Assim , qualquer pessoa mal
 * intencionada que interceptar a comunicação não vai entender o conteúdo.
 * Claro, isso só funciona se o receptor da mensagem souber decifrá-la...
 *
 * Faça um programa que receba como argumento da função main o nome de um
 * arquivo binário e leia deste arquivo uma quantidade indeterminada de
 * registros do tipo mensagem_secreta. Para cada registro, crie um arquivo texto
 * contendo apenas a mensagem secreta decifrada.
 *
 * A cifra é simples: deslocar cada caractere do string (até o caractere de
 * terminação - não incluso) a quantidade "segredo" de caracteres. Por exemplo,
 * um segredo 2 transforma o caractere 'a' em 'c'. Suponha que o segredo é
 * sempre válido (i.e. nunca gera um caractere inválido), ou seja, não se
 * preocupe com os valores. Segue junto a este trabalho o arquivo "teste.bin"
 * para testes. No exemplo, as mensagens decifradas são facilmente reconhecidas
 * e, para facilitar o desenvolvimento, saiba que o primeiro registro tem
 * segredo 0.
 *
 * Cada arquivo texto deve ter o nome conforme o seguinte padrão:
 * "nome_do_binario-#.txt", em que "nome_do_binario" é o nome do arquivo binário
 * de origem, e # é a posição do registro em questão neste arquivo binário. Como
 * exemplo, veja o arquivo "teste.bin-0.txt". Caso não seja possível criar um
 * arquivo texto, exiba uma mensagem indicando qual arquivo deixou de ser criado
 * e continue o processamento dos demais registros.
 *
 * Suponha que todos os caracteres da mensagem são ASCII.
 *
 ***********
 * ATENÇÃO *
 ***********
 * O registro é definido com a opção __attribute__ ((packed)). Você pode ignorar
 * isto e continuar a programar como sempre fez ou aproveitar a chance de
 * aprender algo novo e ler:
 *     https://en.wikipedia.org/wiki/Sizeof#Structure_padding                 */

#include <stdio.h>

typedef struct {
	int segredo;
	char mensagem[101];
} __attribute__ ((packed)) mensagem_secreta;

int main(int argc, char **argv) {
	/* Validação de entradas:
	   - testar se os argumentos são suficientes
	   - testar se os argumentos são válidos */

	/* Leitura de quantidade indeterminada de registros do arquivo dado.
	 * (veja o que retorna a função fread) */

	/* Escrita de cada mensagem em arquivo texto apropriado.
	 * (veja a função sprintf) */

    return 0;
}
