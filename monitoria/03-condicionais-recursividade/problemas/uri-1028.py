"""
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a%b)
"""


def mdc(a, b):
    return a if b == 0 else mdc(b, a % b)


a, b = map(int, input().split())
print(mdc(a, b))
