# Entrada de dados do usuário
saldoAtual = float(input("Digite o saldo atual: "))
valorDeposito = float(input("Digite o valor do depósito: "))
valorRetirada = float(input("Digite o valor da retirada: "))

# Cálculo do saldo final
saldoFinal = saldoAtual + valorDeposito - valorRetirada

# Exibe o resultado formatado com uma casa decimal
print(f"Saldo atualizado na conta: {saldoFinal:.1f}")

