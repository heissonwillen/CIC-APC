p_a, p_b, t_a, t_b = [float(i) for i in input().split()]

tempo_decorrido = 0

while True:
    if (t_b > t_a) or int(p_a+p_a*t_a/100) == p_a:
        print('A nunca alcancara B.')
        break

    p_a, p_b = int(p_a+p_a*t_a/100), int(p_b+p_b*t_b/100)
    tempo_decorrido += 1

    if p_a >= p_b:
        if tempo_decorrido > 1000:
            print('Mais de um milenio.')
        else:
            print(f'Vai alcancar em {tempo_decorrido} ano(s).')
        break
