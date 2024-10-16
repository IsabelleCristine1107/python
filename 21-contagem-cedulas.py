valor_pagamento = int(input("Digite o valor do pagamento (inteiro positivo): "))

if valor_pagamento <= 0:
    print("Por favor, insira um valor inteiro positivo.")
else:
    cedula_50 = valor_pagamento // 50
    valor_pagamento %= 50
    cedula_20 = valor_pagamento // 20
    valor_pagamento %= 20
    cedula_10 = valor_pagamento // 10
    valor_pagamento %= 10
    cedula_5 = valor_pagamento // 5
    valor_pagamento %= 5
    cedula_1 = valor_pagamento

    print("Quantidade mínima de cédulas necessárias:")
    print(f"50 R$: {cedula_50}")
    print(f"20 R$: {cedula_20}")
    print(f"10 R$: {cedula_10}")
    print(f"5 R$: {cedula_5}")
    print(f"1 R$: {cedula_1}")