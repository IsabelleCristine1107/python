def par(x):
    return x % 2 == 0


def par_ou_impar(x):
    if par(x):
        return "par"
    else:
        return "impar"


valor = 0
while valor != '5':
    Valor = input("Digite um valor ou '5' para sair: ")
    if Valor != '5':
        print(par_ou_impar(int(valor)))
    else:
        print("Fim do programa")
