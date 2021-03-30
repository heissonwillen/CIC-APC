def is_power(a, b):
    if a == b:
        return True
    if not(a % b == 0):
        return False
    return is_power(a // b, b)


print(is_power(21, 3))
