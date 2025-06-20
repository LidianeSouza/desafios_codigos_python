# 💰 Condicionalmente Rico: Tomadas de Decisão no Código

## 📌 Descrição
Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint. Como desenvolvedor da empresa, você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso. 

## ⚙️ Regras do Saque
- Cada cliente digitará o valor do seu `saldoTotal` e o `valorSaque`.
- Um saque só pode ser realizado se o `saldoDisponível` na conta for igual ou superior ao valor solicitado.
- Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado. 
- Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida. 

## ⌨️ Entrada
A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.

## 🖥️ Saída
- Se o saque for realizado com sucesso, exibir a mensagem:  
  `"✅ Saque realizado com sucesso! Novo saldo: {saldo}"`  
  Onde `{saldo}` é o novo saldo disponível na conta.  
- Se o saque não for possível devido a saldo insuficiente, exibir a mensagem:  
  `"❌ Saldo insuficiente. Saque não realizado!"`

## 📊 Exemplos
| 🏦 Entrada | 🏧 Saída |
|------------|---------|
| `1000` <br> `200` | `"✅ Saque realizado com sucesso! Novo saldo: 800"` |
| `1500` <br> `1800` | `"❌ Saldo insuficiente. Saque não realizado!"` |
| `300` <br> `200` | `"✅ Saque realizado com sucesso! Novo saldo: 100"` |
