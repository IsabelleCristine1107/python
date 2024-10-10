Contador = 0

while Contador <= 10:
    Contador += 1
    if Contador == 6:
        print("Não vou mostrar o 6.")
        continue # Interrompe a interação atual e volta para
    if Contador >= 10 and Contador <= 27:
        print('Não vou mostrar o 0', Contador)
        continue # Interrompe a interação atual e volta por
    print(Contador)
    if Contador == 48:
        break #Interrompe o loop complemente quando
print('Acabou')
