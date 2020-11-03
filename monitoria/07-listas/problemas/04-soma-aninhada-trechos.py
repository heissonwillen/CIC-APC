
def nested_sum(t):
  soma = 0
  for i in range(len(t)):
    valor = t[i]
    soma += sum(valor)
  print(soma)

def nested_sum1(t):
  soma = 0
  for elemento in t:
    soma += elemento
  print(soma)

def nested_sum2(t):
  soma = 0
  for elemento in t:
    for el in elemento:
      if isinstance(el, int) or isinstance(el, float):
        soma += el
  print(soma)

def neste_sum3(t):
  pass

t = [[1, 2], [3], [4, 5, '6']]

#nested_sum(t)
#nested_sum1(t)
nested_sum2(t)
