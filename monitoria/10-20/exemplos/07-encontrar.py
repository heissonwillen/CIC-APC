'''
Como exercício, altere find para que tenha um terceiro parâmetro: o índice em word onde deve começar a busca.
'''

def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return-1

# print(find('banana','a', ))
print(find('banana','a', 2))
