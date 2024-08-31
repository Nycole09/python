#atividade 1
nome = str(input("escreva um nome completo: "))
textMauis = nome.upper()
neMinu = nome.lower()
nomeSE = nome.replace(" ", "")
splitNome = nome.split()
len(nome)
print(f'{nome}, com letras maiusculas: {textMauis}, e com letras minusculas: {neMinu}, e o nome sem espaços é:  {nomeSE}, primeiro nome : {splitNome[0]}')

#atividade 02
nomecity = str(input("digite o nome de uma cidade: "))
nomeCity1 = nomecity.lower()
sobCity = "santo"
splitCity = nomeCity1.split()
verificacaoCity = sobCity in splitCity[0] 
print(f'essa cidade começa com Santo? {verificacaoCity}')



#atividade 03
nome1 = str(input('digite um nome: '))
nome2 = nome1.lower()
sobreNome = 'silva'
verificacaoNome = sobreNome in nome2 
print(f'esse nome tem silva? {verificacaoNome}')

#atividade 04
teclado = str(input('digite uma palavra: '))
letra = "a"
teclado1 = teclado.lower()
qtdLetrasa = teclado1.count(letra)
posicaoPalavra = teclado1.find(letra)
posicaoPalavra2 = teclado1.rfind(letra)
print(f'A quantidade de letra A é: {qtdLetrasa} e {letra} posição é: {posicaoPalavra+1}, e a posição da ultima {letra} é: {posicaoPalavra2+1} ')

#atividade 05
nomeComp = str(input("digite nome completo "))
lNome = nomeComp.split()
print(f'O primeiro nome é: {lNome[0]}')
print(f'O ultimo nome é: {lNome[-1]}')