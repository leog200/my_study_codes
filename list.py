#Exemplo Lista
#Lista é uma coleção ordenada e mutável. Permite membros duplicados
#Usa-se sempre os colchetes para armazenar os valores dentro da lista
#type() serve para mostrar o tipo de cada valor

lista = ["carro", 2, 55.98, True or False]
print(type(lista))

for itens_lista in lista:
    print(type(itens_lista)) 

#-----------------------------------------------------#

times = ["Internacional", "grêmio", "Santos"]

print("Times disponíveis: ")
for clubes in times:
    print(clubes)


clube_escolhido = input("Qual clube você escolhe?")


if clube_escolhido =="Internacional":
    print("Campeão de Tudo!")
elif clube_escolhido == "grêmio":
    print("TRI REBAIXADO")
elif clube_escolhido == "Santos":
    print("Vai Santos")
else:
    print("Clube não encontrado na lista.")


    