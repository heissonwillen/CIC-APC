"""
Recebemos uma string S que consiste em N letras. Queremos encontrar a maior letra alfabética que ocorre tanto em minúsculas quanto em maiúsculas em S, ou decidir que não existe tal letra,

Nota: Uma letra é alfabeticamente maior do que outra se ocorrer posteriormente na ordem alfabética do inglês. Por exemplo, “E” é alfabeticamente maior do que “B”.

Escreva uma função: “solution(s)”

que, dada uma string S, retorna uma string que consiste em uma letra - a maior alfabeticamente de todas as letras que ocorrem tanto em minúsculas quanto em maiúsculas em S. A letra retornada ser maiúscula,

Se essa letra não existir, a função deve retornar "NO".

Exemplos:

1. Dado S = “aaBabcDaA”, sua função deve retornar "B". As letras que ocorrem tanto em minúsculas quanto em maiúsculas são: "A", "B" ("B" é alfabeticamente maior)

2. Dado S = "Codility", sua função deve retornar "NO". Não há nenhuma letra que ocorra tanto em minúsculas quanto em maiúsculas.

3. Dado S = “WeTestCodErs", sua função deve retornar “T”. As letras que ocorrem tanto em minúsculas quanto em maiúsculas são: “E”, “T” (T é alfabeticamente maior)
"""


def solution(s):
    s = list(s)
    s.sort(reverse=True)

    s_lower = [item for item in s if item.islower()]

    for item in s_lower:
        if item.upper() in s:
            return item.upper()

    return 'NO'


print(solution('aaBabcDaA'))
print(solution('Codility'))
print(solution('WeTestCodErs'))
