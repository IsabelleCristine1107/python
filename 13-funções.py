# Declaração da função exibirMensagem(nome)
def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")


# Início do meu algoritmo
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade:")
exibirMensagem(nome, idade) #Exibe a mensagem com o nome do usuário.

# Chamando função com retorno
ValorA = int(input("Digite o primeiro número: "))
ValorB = int(input("Digite o segundo número: "))
resultado = somar(ValorA, ValorB)
print(f"O resultado da soma = {resultado}")