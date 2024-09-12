# IMC
# Ler peso e altura
# Calcule o IMC

print("Programa para Calculo de IMC")
Peso = float(input("Digite o seu peso (em kg): "))
Altura = float(input("Digite a sua altura(em metros) "))
Imc = Peso / (Altura**2)

print(f"Seu Imc é {Imc: .2f}")  # .2f é usado
# para mostrar apenas duas casas decimais

if (Imc < 18.5):
    print("Abaixo do peso")
elif (18.5 <= Imc < 25):
    print("Peso normal")
elif (25 <= Imc < 35):
    print("Sobrepeso")
else:
    print("Obesidade")  # else é usado para a ultima condição
