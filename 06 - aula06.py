# Voto Obrigatório
# Opcional: entre 16 e 17 e a partir de 65
# Não permitido: menores de 16 anos

print("Voto Obrigatório")

idade = int(input("Digite a sua idade: "))

if (idade >= 18 and idade < 65):
    print("Voto Obrigatório!")
elif (16 <= idade < 18 or idade >= 65):
    print("Voto Opcional!")
else:
    print("Voto não permitido!")
