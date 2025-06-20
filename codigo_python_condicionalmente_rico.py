# Solicita os dados do usuário
saldoTotal = int(input("Digite o saldo da conta: "))
valorSaque = int(input("Digite o valor do saque: "))

# Verifica se o saque pode ser realizado
if saldoTotal >= valorSaque:
    novoSaldo = saldoTotal - valorSaque
    print(f"✅ Saque realizado com sucesso! Novo saldo: {novoSaldo}")
else:
    print("❌ Saldo insuficiente. Saque não realizado!")
