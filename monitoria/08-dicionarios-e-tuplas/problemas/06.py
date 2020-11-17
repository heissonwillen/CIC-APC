# palavra = 'vanessa'

# dic = {}
# for letra in palavra:
#     if letra not in dic:
#       dic[letra] = 1
#     else:
#       dic[letra] += 1
# print(dic)

palavra = 'vanessa'

dic = {}
for letra in palavra:
	dic[letra] = dic.get(letra, 0) + 1

print(dic)



