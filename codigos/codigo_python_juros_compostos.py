def calcular_juros_compostos(valor_inicial, taxa_juros, periodo):
    valor_final = valor_inicial * (1 + taxa_juros) ** periodo
    print(f"Valor final do investimento: R$ {valor_final:.2f}")

# Exemplos de uso
calcular_juros_compostos(5000, 0.08, 5)
calcular_juros_compostos(1000, 0.06, 3)
calcular_juros_compostos(20000, 0.04, 10)

