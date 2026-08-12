custo = int(input("Digite o custo do carro: "))

print("A distribuição eh 15% do valor do custo")
distribuidor = (custo*12)/100

print ("Valor distrribuicao:", distribuidor)

print("Os impostos são 30% do valor de fabrica")
impostos = (custo*12)/100

print ("Valor imposto: ", impostos)

valorFinal = distribuidor+custo+impostos

print("O valor final para o consumidor vai ser de: ",valorFinal)