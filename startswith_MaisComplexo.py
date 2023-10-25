#Exemplo mais complexo sobre startswith()

#Lista de nomes de países
paises = ["Brasil", "Estados Unidos", "Canadá", "Alemanha", "Espanha", "Itália"]

#Filtrar países que começam com "E"
paises_com_e = [pais for pais in paises if pais.startswith("E")]

#Exibir os países que começam com "E"
print("Países que começam com 'E':")
for pais in paises_com_e:
    print(pais)
