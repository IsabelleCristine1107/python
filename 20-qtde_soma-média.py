# Programa que leia números inteiros
# Exiba a quantidade de números digitados assim que for colocado 0, indicando o fim da digitação
#Exibe a soma e a média aritmética

numeros = []

while True:
    numero = input("Digite um número inteiro (0 para sair): ")
    if numero == '0':
        break
    if numero.lstrip('-').isdigit():
        numeros.append(int(numero))

quantidade = len(numeros)
soma = sum(numeros)
media = soma / quantidade if quantidade > 0 else 0

print(f"Quantidade de números digitados: {quantidade}")
print(f"Soma dos números: {soma}")
print(f"Média aritmética: {media:.2f}"),