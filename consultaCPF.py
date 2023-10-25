#Neste código iremos fazer uma consulta de CPF, se é um CPF válido ou inválido

def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifiqua se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verifiqua se todos os dígitos são iguais (CPF inválido)
    if cpf == cpf[0] * 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Verifiqua o primeiro dígito verificador
    if int(cpf[9]) != digito1:
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifiqua o segundo dígito verificador
    if int(cpf[10]) != digito2:
        return False

    # Se todas as verificações passaram, o CPF é válido
    return True

# Exemplo de uso:
cpf = input("Digite um CPF para validar: ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
