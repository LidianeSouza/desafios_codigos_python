# 🏦 O Grande Depósito - Solucionando Problemas Bancários

## 📌 Descrição  
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a **realizar depósitos** em suas contas. O programa deve solicitar ao cliente o valor do depósito e **verificar se o valor é válido**.  

✅ Se o valor for **maior do que zero**, o programa deve **adicionar o valor ao saldo da conta**.  
❌ Caso contrário, o programa deve **exibir uma mensagem de erro**.  
🔄 O programa deve solicitar apenas **uma vez** o valor do depósito.  

## 📥 Entrada  
O programa deve receber o **valor do depósito digitado pelo cliente**.  
O valor pode ser **decimal**, representando o valor em reais.  

## 📤 Saída  
- Se um **valor válido** for informado, o programa deve exibir uma mensagem de **sucesso** e o saldo da conta atualizado.  
- Se o valor for `"0"`, deverá imprimir uma mensagem **encerrando o programa**.  
- Caso um **valor inválido** seja digitado, o programa deve **exibir uma mensagem de erro** solicitando um novo valor.  

## 📊 Exemplos  
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| 💵 Entrada | 🏧 Saída |
|------------|---------|
| `500.50` | `"Depósito realizado com sucesso! Saldo atual: R$ 500.50"` |
| `-100` | `"Valor inválido! Digite um valor maior que zero."` |
| `0` | `"Encerrando o programa..."` |


