#Este código mostra as diferenças entre se usar uma lista normal e uma list comprehension. 

#lista normal
lista_precos = [200, 400, 600, 800, 1000]
nova_lista_precos = []
for preco in lista_precos:
    nova_lista_precos.append(preco * 2)
print(nova_lista_precos)


#list comprehension
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)

#lista normal
imposto = [1000, 4000, 2000, 200]
for preco in imposto:
    if preco > 1000:
        imposto.append(preco * 0.5)
    print(imposto)

#list comprehension
imposto2 = [preco * 0.5 for preco in imposto if preco > 1000]
print(imposto2)
