a = float(input("Informe o Coeficiente a:"))
a = float(input("Informe o Coeficiente b:"))
a = float(input("Informe o Coeficiente c:"))

# cálculo de delta
delta = b**2 - 4*a*c

#Verificando o delta
if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"A única raiz real é {x}")
else:
    x1 = (-b + delta ** 0.5) / (2 * a)
    x2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As raízes reais são {x1} e {x2}")