variavel = 100

while True:
	print("Ainda estamos no loop")
	a = int(input())

	variavel = variavel - a

	if variavel > 0:
		break

print("Saimos do loop")

