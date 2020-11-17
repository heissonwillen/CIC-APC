import turtle


def pegar_coordenadas():
    with open('lab.dat', 'r') as arquivo:
        return [tuple(map(int, linha.split())) for linha in arquivo.readlines()]


def plot_regressao():
    coords = pegar_coordenadas()
    x_medio = sum([coord[0] for coord in coords])/len(coords)
    y_medio = sum([coord[1] for coord in coords])/len(coords)

    m = sum([(x*y-x_medio*y_medio)/(x**2-x_medio**2) for x, y in coords])

    wn = turtle.Screen()
    alex = turtle.Turtle()
    turtle.setworldcoordinates(0, -1500, 100, 1500)

    # for coord in coords:
    #     alex.setpos(coord)
    #     alex.dot()

    for x in range(100):
    	alex.setpos(x, y_medio+m*(x-x_medio))
    	alex.dot()
    	# print(x, y_medio+m*(x-x_medio))
    	# alex.setpos(x,x)
    	# alex.dot()

    wn.exitonclick()


plot_regressao()
