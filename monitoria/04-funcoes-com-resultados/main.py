"Um número a é uma potência de b se for divisível por b e a/b for uma potência de b"


def is_power(a, b):
    if a == b:
        return True
    if a % b != 0:
        return False
    return is_power(a // b, b)


print(is_power(25, 5))
