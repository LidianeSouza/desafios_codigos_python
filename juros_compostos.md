# 📈 Juros Compostos 

## 📌 Descrição

Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os **juros compostos** de um investimento. Seu objetivo é criar uma função que receba três parâmetros:  
1️⃣ **Valor inicial do investimento**  
2️⃣ **Taxa de juros anual**  
3️⃣ **Período de tempo em anos**  
A função deve calcular e retornar o **valor final do investimento** após o período determinado, levando em consideração os juros compostos. 

## 📥 Entrada
A função deve receber os seguintes parâmetros:
- **`valor_inicial`**: um número inteiro ou decimal representando o valor inicial do investimento. 
- **`taxa_juros`**: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de **5%**, o valor passado será **0.05**. 
- **`periodo`**: um número inteiro representando a quantidade de anos do investimento. 

## 📤 Saída
A função deve retornar o **valor final do investimento** após o período determinado, considerando os juros compostos. O valor final deve ser **arredondado para duas casas decimais**. 

## 📊 Exemplos
| 🏦 Entrada | 💵 Saída |
|------------|---------|
| `5000` <br> `0.08` <br> `5` | `"Valor final do investimento: R$ 7346.64"` |
| `1000` <br> `0.06` <br> `3` | `"Valor final do investimento: R$ 1191.02"` |
| `20000` <br> `0.04` <br> `10` | `"Valor final do investimento: R$ 29604.89"` |

