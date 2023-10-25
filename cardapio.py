#Código básico que mostra as opções de um cardápio

def cardapio(opcoes):

    mostrar = input("Você deseja visualizar o cardápio? S/N:")

    if mostrar.upper() == "S":
        print(f"Cardápio: {opcoes}.")
    else:  
        print("Até mais!")

opcoes = "1 - Carne de gado, 2 - Carne de porco, 3 -  Carne de ovelha"
cardapio(opcoes)
