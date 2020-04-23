for i in range (100):
	print(["{} é ímpar".format(i), "{} é par".format(i)][i % 2 == 0])