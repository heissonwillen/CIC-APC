def quantos_semestres(semestre_atual, ano_atual, matricula):
    ano_entrada = int(matricula[0] + matricula[1])
    sem_entrada = int(matricula[3])

    ano_atual -= 2000

    print(ano_entrada)
    print(ano_atual)

    q_sem = (ano_atual - ano_entrada) * 2 + semestre_atual - sem_entrada

    print(q_sem)


quantos_semestres(1, 2020, '190014181')
