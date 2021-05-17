from statistics import mean, pstdev

OBJETOS = ['bison', 'elephant', 'horse', 'ibis', 'sky', 'mountain', 'building',
           'flower', 'sand', 'tree', 'field', 'road', 'tower', 'ocean', 'cliff', 'waterfall']


def log(d, f=True):
    for k in d:
        print(k, ' '.join(
            map(lambda s: f'{str(round(s, 1) if f else int(s))}', d[k])))


def indicadores(dados):
    ind = {}
    for linha in dados:
        nome, objeto = linha[0], linha[1].split('-')[-1]
        ind[nome] = ind.get(nome, [0.0]*len(OBJETOS))
        ind[nome][OBJETOS.index(objeto)] = 1.0

    return ind


def indicadores(dados):
    ind = {}
    for linha in dados:
        nome, objeto = linha[0], linha[1].split('-')[-1]
        ind[nome] = ind.get(nome, [0.0]*len(OBJETOS))
        ind[nome][OBJETOS.index(objeto)] = 1.0

    return ind


def estatistica(dados):
    coords = {}
    for linha in dados:
        coords[linha[0]] = coords.get(linha[0], [])
        coords[linha[0]].append(linha[2:])

    est = {}
    for nome in coords:
        est[nome] = [
            len([c for c in coords[nome]])/2,
            mean([(c[0]+c[2])/2 for c in coords[nome]])/128,
            mean([(c[1]+c[3])/2 for c in coords[nome]])/128,
            mean([c[2]-c[0] for c in coords[nome]])/128,
            mean([c[3]-c[1] for c in coords[nome]])/128,
            mean([(c[2]-c[0])*(c[3]-c[1]) for c in coords[nome]])/(128**2),
            pstdev([(c[0]+c[2])/2 for c in coords[nome]])/32,
            pstdev([(c[1]+c[3])/2 for c in coords[nome]])/32,
            pstdev([c[2]-c[0] for c in coords[nome]])/32,
            pstdev([c[3]-c[1] for c in coords[nome]])/32,
        ]

    return est


def vetor_medio(ind, est):
    vec = [ind[k] + est[k] for k in ind.keys()]
    return [mean([vec[j][i] for j in range(len(vec))]) for i in range(len(vec[0]))]


def dist(p, q):
    return sum([abs(a - b) for a, b in zip(p, q)])


def amostras(ind, est):
    vec = [ind[k] + est[k] for k in ind.keys()]
    dists = [sum([dist(vec[i], vec[j]) for j in range(len(vec))])
             for i in range(len(vec))]

    return list(ind.keys())[dists.index(min(dists))]


t, n = map(int, input().split())
dados = []
for _ in range(n):
    input()
    linha = []
    linha.append(input())
    linha.append(input())
    linha.extend([int(x) for x in input().split()])
    dados.append(linha)


if t == 1:
    log(indicadores(dados), False)
if t == 2:
    log(estatistica(dados))
if t == 3:
    v = vetor_medio(indicadores(dados), estatistica(dados))
    print(' '.join(map(lambda s: str(round(s, 1)), v)))
if t == 4:
    print(amostras(indicadores(dados), estatistica(dados)))
