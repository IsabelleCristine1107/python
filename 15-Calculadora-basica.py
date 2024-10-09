# Deinição das funções

#Função exibir menu
def exibirMenu():
    print("CALCULADORA DAS OPERAÇÕES BÁSICAS")
    print("Menu de escolha:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Resto da Divisão")
    print("6. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha


def soma(n1, n2):
    return n1 + n2


def subtração(n1, n2):
    return n1 - n2


def multipliacação(n1, n2):
    return n1 * n2


def divisão(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Erro: Divisão por zero não é permitida."
    

    def resto_devisão(n1, n2):
        if n2 != 0:
            return n1 % n2
        else:
            return "Erro: Divisão por zero não é permitida"
        

# Declaração de variáveis
opção = 0
n1 = 0
n2 = 0

# Início de código
while opção != 6:
    opção = exibirMenu()

    if opção in [1, 2, 3, 4, 5,]:
        n1 = float(input("Insira o primeiro valor: "))
        n2 = float(input("Insira o segundo valor: "))

    if opção == 1:
        print(f"A soma dos valores é: {soma (n1, n2)}\n")
    elif opção == 2:
        print(f"A subtração dos valores é: {subtração(n1, n2)}\n")
    elif opção == 3:
        print(f"A multipliacação dos valores é: {multipliacação(n1, n2)}\n")
    elif opção == 4:
        print(f"A divisão dos valores é: {divisão(n1, n2)}\n")
    elif opção == 5:
        print(f"O resto da divisâo dos valores é: {resto_divisão(n1, n2)}\n")
    elif opção == 6:
        print("Finalizando o código!")
    else:
        print("Opção inválida. Tente novamente. \n") 