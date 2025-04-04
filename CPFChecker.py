def validar_cpf(cpf: str) -> bool:
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))
    
    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Verifica se todos os dígitos são diferentes (caso contrário é inválido)
    if cpf == cpf[0] * 11:
        return False
    
    # Função para calcular um dígito verificador
    def calcular_digito(cpf_parcial, peso_inicial):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf_parcial, range(peso_inicial, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)
    
    # Calcula o primeiro dígito verificador
    primeiro_digito = calcular_digito(cpf[:9], 10)
    # Calcula o segundo dígito verificador
    segundo_digito = calcular_digito(cpf[:9] + primeiro_digito, 11)
    
    # Verifica se os dígitos calculados são iguais aos dígitos fornecidos
    return cpf[-2:] == primeiro_digito + segundo_digito

# Exemplo de uso
print("Tool made by: https://github.com/GabrielConforto")
print("-------------------------------------------------")
cpf = input("Digite o CPF para validar:")
print("-----------------------")
if validar_cpf(cpf):
    print("O CPF é válido.")
else:
    print("O CPF é inválido.")
