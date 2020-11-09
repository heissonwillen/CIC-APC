'''
https://panda.ime.usp.br/pensepy/static/pensepy/11-Dicionarios/dicionarios.html
'''

'''
your professor is my student
>>> yer foul blaggart be me swabbie

hello sir
>>> avast matey
'''

tradutor = {
    'sir': 'matey',
    'hotel': 'fleabag inn',
    'student': 'swabbie',
    'boy': 'matey',
    'madam': 'proud beauty',
    'professor': 'foul blaggart',
    'restaurant': 'galley',
    'your': 'yer',
    'excuse': 'arr',
    'students': 'swabbies',
    'are': 'be',
    'lawyer': 'foul blaggart',
    'the': 'th’',
    'restroom': 'head',
    'my': 'me',
    'hello': 'avast',
    'is': 'be',
    'man': 'matey',
}

s = input().split()

for palavra in s:
    print(tradutor[palavra], end=' ')

print()
