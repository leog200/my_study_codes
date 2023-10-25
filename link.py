#Código simples que pede ao usuário adicionar links em uma lista

# Cria uma lista vazia para armazenar os links
lista_links = []

# Cria uma função para inserir links na lista
def inserir_link():
    link = input("Digite aqui qual link você deseja inserir: ")
    lista_links.append(link)
    print("Link inserido com sucesso!")

# Cria uma função para mostrar os links armazenados na lista
def mostrar_links():
    print("Links armazenados:")
    for link in lista_links:
        print(link)

# Loop principal do programa
while True:
    print("\nEscolha uma opção:")
    print("1. Inserir um link")
    print("2. Mostrar links armazenados")
    print("3. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        inserir_link()

    elif escolha =="2":
        mostrar_links()

    elif escolha == "3":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção Inválida. Tente novamente.")