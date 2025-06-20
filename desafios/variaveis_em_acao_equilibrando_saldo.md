# 💰 Variáveis em Ação: Equilibrando o Saldo

## 📌 Descrição
Uma empresa bancária identificou a necessidade de desenvolver uma solução que permita ao cliente **equilibrar seu saldo bancário**. O programa deve solicitar:
1. O saldo atual do funcionário.
2. O valor de duas transações: um **depósito** e um **saque**.
3. Atualizar o saldo com base nas transações e exibir o saldo final.

### 🔹 Informação Importante
- O **depósito** deve ser tratado como um valor **positivo**.
- O **saque** deve ser tratado como um valor **negativo**.
- O cálculo do saldo final deve garantir uma saída correta.

## 📥 Entrada
- `saldoAtual`: Um número decimal representando o saldo atual da conta bancária.
- `valorDeposito`: Um número decimal representando o valor a ser depositado na conta.
- `valorRetirada`: Um número decimal representando o valor a ser retirado da conta.

### ⚠️ Regra de Formatação
O saldo final deve ser formatado com **apenas uma casa decimal**.

## 📤 Saída
Um número decimal que representa o **saldo atualizado** na conta bancária após o processamento das transações.

## 🔎 Exemplos

| **Entrada**                | **Saída**                          |
|----------------------------|-----------------------------------|
| `1000` <br> `500` <br> `200` | `Saldo atualizado na conta: 1300.0` |
| `100` <br> `10` <br> `50`   | `Saldo atualizado na conta: 60.0`  |
| `4000` <br> `1500` <br> `200` | `Saldo atualizado na conta: 5300.0` |

---

