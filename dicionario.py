#O dicionário é uma coleção ordenada e imutável. Nenhum membro duplicado.

emails = {
    "Prefeitura": "prefeitura@gmail.com",
    "Igreja": "igreja@gmail.com",
    "Pizzaria": "pizzaria@gmail.com"

}

#Para adicionar um novo email ao dicionario
emails["Shopping"] = "shopping@gmail.com"
print(emails)


#Para mostrar um email especifico que esteja no dicionario
email = emails['Igreja']
print(email)


#Para mostrar todas as Chaves pertencentes no dicionario
#Ex: 1
for chaves_dicionario in emails:
    print(chaves_dicionario)

#Ex: 2
print(emails.keys())

#Para mostrar todos os emails pertencentes no dicionario
#Ex: 1
for valores_chaves in emails:
    email = emails[valores_chaves]
    print(email)

#Ex:2
    print(emails.values())


#Retirar um email do dicionario
emails.pop("Prefeitura")
print(emails)

#Verificar chave existente no dicionario
if "Pizzaria" in emails:
    print("Existe.")
else:
    print("Não Existe.")

#Verificar email(valor) existente no dicionario
if "pizzaria@gmail.com" in emails.values():
    print("Existe.")
else:
    print("Não Existe.")
