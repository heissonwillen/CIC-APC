string = '10nome5casa20'

numeros = ''
for c in string:
    numeros += c if c.isnumeric() else ' '

print(numeros.split())
