# Lê a quantidade de ativos
quantidade = int(input("Digite a quantidade de ativos: "))

# Cria uma lista vazia para armazenar os ativos
ativos = []

# Lê cada ativo do usuário e adiciona à lista
for i in range(quantidade):
    ativo = input(f"Digite o ativo {i + 1}: ")
    ativos.append(ativo)

# Ordena a lista em ordem alfabética
ativos.sort()

# Exibe os ativos em ordem, um por linha
print("\nAtivos organizados:")
for ativo in ativos:
    print(ativo)
