#Código parecido com o do arquivo link.py, porém esse permite acessar o link no browser 

import webbrowser

# Cria uma lista vazia para armazenar os links
lista_de_links = []

# Cria uma função para inserir links na lista
def inserir_link():
    link = input("Digite o link que deseja inserir: ")
    lista_de_links.append(link)
    print("Link inserido com sucesso!")

# Cria uma função para mostrar os links armazenados na lista
def mostrar_links():
    print("Links armazenados:")
    for i, link in enumerate(lista_de_links, start=1):
        print(f"{i}. {link}")

# Cria uma função para abrir um link pelo índice
def abrir_link():
    try:
        indice = int(input("Digite o número do link que deseja abrir: "))
        if 1 <= indice <= len(lista_de_links):
            webbrowser.open(lista_de_links[indice - 1])
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Inserir um link")
    print("2. Mostrar links armazenados")
    print("3. Abrir um link")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        inserir_link()
    elif escolha == "2":
        mostrar_links()
    elif escolha == "3":
        abrir_link()
    elif escolha == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
