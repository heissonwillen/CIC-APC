import turtle


def pegar_coordenadas():
    coordenadas = []
    with open('misterio.dat', 'r') as arquivo:
        for linha in arquivo.readlines():
            if ('CIMA' in linha or 'BAIXO' in linha):
                coordenadas.append(linha)
            else:
                coordenadas.append(tuple(map(int, linha.split())))

        return coordenadas

def desenhar():
    coordenadas = pegar_coordenadas()

    wn = turtle.Screen()
    alex = turtle.Turtle()
    turtle.setworldcoordinates(-250, -250, 400, 200)

    for coordenada in coordenadas:
        if not isinstance(coordenada, str):
            print(coordenada)
            alex.setpos(coordenada)

    wn.exitonclick()


desenhar()
