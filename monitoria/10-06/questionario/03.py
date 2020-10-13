def pattern(n):
    print(n)
    if n <= 0:
        return
    pattern(n-5)

pattern(16)
