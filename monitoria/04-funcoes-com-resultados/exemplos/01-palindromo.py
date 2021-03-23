def first(word):
    return word[0]


def last(word):
    return word[-1]


def middle(word):
    return word[1:-1]


# def palindrome(word):
#     if len(word) < 2:
#         return True
#     if not (last(word) == first(word)):
#         return False
#     return palindrome(middle(word))

def palindrome(w):
    return len(w) < 2 or first(w) == last(w) and palindrome(middle(w))


print(palindrome('osso'))
print(palindrome('a'))
print(palindrome('batata'))
