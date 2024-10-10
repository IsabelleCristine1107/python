# Algoritmo que coverte em Python temperaturas em escalas Celsius, Fahrenheit e Kelvin
# Apresenta um Menu recursivo

def Farenheit_para_Kelvin(F):
    K = (F-32)*5/9+273.15
    return (K)

def Farenheit_para_Celsius(F):
    C = (F-32)*5/9
    return (C)

def Kelvin_para_Farenheit(K):
    F = (K-273.15)*9/5+32
    return (F)

def Kelvin_para_Celsius(K):
    C = K-273.15
    return (C)

def Celsius_para_Farenheit(C):
    F = c*9/5+32
    return (F)

def Celsius_para_Kelvin(C):
    K = C+273.15
    return (K)

def Menu():
    print("Escolha a opção desejada:")
    print("1 - Converter de Farenheit para Kelvin")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Converter de Kelvin para Farenheit")
    print("4 - Converter de Kelvin para Celsius")
    print("5  - Converter de Celsius para Farenheit")
    print("6 - Converter de Celsius para Kelvin")
    print("7 - Sair")

while True:
    Menu()
    opcao =  input("Escolha a opção: ")
    
    if opcao == 1:
        F = float(input("Digite a temperatura em Farenheit: "))
        K =  Farenheit_para_Kelvin(F)
        print(f"A temperatura em Kelvin é: {K} K")
    elif opcao  == 2:
        F = float(input("Digite a temperatura em Farenheit: "))
        C = Farenheit_para_Celsius(F)
        print(f"A temperatura em Celsius é: {C} C")
    elif opcao == 3:
        K  = float(input("Digite a temperatura em Kelvin: "))
        F = Kelvin_para_Farenheit(K)
        print(f"A temperatura em Farenheit é: {F} F")
    elif opcao  == 4:
        K = float(input("Digite a temperatura em Kelvin: "))
        C = Kelvin_para_Celsius(K)
        print(f"A temperatura em Celsius é: {C} C")
    elif opcao == 5:
        



