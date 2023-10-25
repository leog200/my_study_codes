#Neste código iremos calcular os tributos cobrados encima de valor x

def calcular_tributos(valor):
    #Definindo as taxas de imposto
    taxa_imposto_federal = float(input("Informe a taxa de imposto federal: "))
    taxa_imposto_estadual = float(input("Informe a taxa de imposto estadula: "))
    taxa_imposto_municipal = float(input("Informe a taxa de imposto municipal: "))

    #Calculando os valores de cada imposto
    imposto_federal = valor * taxa_imposto_federal
    imposto_estadual = valor * taxa_imposto_estadual
    imposto_municipal = valor * taxa_imposto_municipal

    #Calculando o total de impostos
    total_impostos = imposto_federal + imposto_estadual + imposto_municipal

    return total_impostos

def main():
    valor_transacao = float(input("Digite o valor da transação: R$ "))
    
    total_impostos = calcular_tributos(valor_transacao)
    
    print(f"Valor da transação: R$ {valor_transacao:.2f}")
    print(f"Total de tributos: R$ {total_impostos:.2f}")

if __name__ == "__main__":
    main()
