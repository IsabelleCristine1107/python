# 09-rent-car.py = escreva um programa que pergunta a quantidade e km
# percorrido por um carro algugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o
# carro custa R$ 60 por dia + R$ 0,15 por km rodado.

#Variáveis
dias_locados = int(input("Dias alugados"))
km_percorridos = float(input("Quantos km foram percorridos?"))

#Cálculo do preço total
total = (dias_locados*60)+(km_percorridos*0.15)
print(f"O valor total a pagar é R${total:.2f}")