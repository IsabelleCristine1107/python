# Tipos de Dados Primitivos:
# - Inteiro (int): números inteiros
# - Float (float): números reais, decimais
# - String (str): Cadeia de caracteres, utilizanndo aspas
# - Boolean (bool): tipo lógico True ou False
# - Complex (complex): números complexos, com parte real ou imaginaria
# - List (list): lista de elementos, ordenados e indexados
# - Tuple (tuple): tupla de elementos, ordenados e Instáveis
# - Dictionary (dict): dicionário de elementos, não ordenados e indexados

# Atribuição de variável por captura
nome = input("Digite o seu nome:")
print("Olá", nome)
idade = input("Digite a sua idade:")
print(idade)
altura = input("Digite a sua altura:")
print(type(altura))

# - Exibir na tela
print(f"nome: {nome} idade: {idade} altura: {altura}")

#Exemplo de conversão de string para inteiro
ValorA = int(input("Digite o Valor de A: "))
ValorB = int(input("Digite o Valor de B: "))
resultado = ValorA + ValorB
print(f"A Soma = {resultado}")
# Exemplo de conversão de string para float
ValorA = float(input("Digite o Valor de A: "))
ValorB = float(input("Digite o Valor de B: "))
resultado = ValorA + ValorB
print(f"A soma = {resultado}")
