
# Solicita o valor do depósito
valor = float(input("Digite o valor do depósito: "))

# Verifica e trata o valor informado
if valor > 0:
    print(f"Depósito realizado com sucesso! Saldo atual: R$ {valor:.2f}")
elif valor == 0:
    print("Encerrando o programa...")
else:
    print("Valor inválido! Digite um valor maior que zero.")