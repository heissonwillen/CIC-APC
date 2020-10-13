def acredita(n1, n2):
    if n1 % n2 == 0 and acredita(n1//n2, n2):
        return 'Pode Acreditar'
    return 'Fake News'

print(acredita(8,2))
print(acredita(10,2))
print(acredita(125,5))
