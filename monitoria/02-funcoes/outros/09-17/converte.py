def converte(fahrenheit):
    celsius = (fahrenheit - 32)/ 1.8
    return f'{celsius:.1f}'

print(converte(-1.0))
print(converte(0))
print(converte(32.0))
