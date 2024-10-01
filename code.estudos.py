def calcular():
    print("Bem-vindo à Calculadora!")
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    while True:
        escolha = input("Digite a opção (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                resultado = num1 + num2
                print(f"{num1} + {num2} = {resultado}")

            elif escolha == '2':
                resultado = num1 - num2
                print(f"{num1} - {num2} = {resultado}")

            elif escolha == '3':
                resultado = num1 * num2
                print(f"{num1} * {num2} = {resultado}")

            elif escolha == '4':
                if num2 == 0:
                    print("Erro! Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f"{num1} / {num2} = {resultado}")

            # Perguntar se o usuário deseja continuar
            proseguir = input("Deseja realizar outra operação? (s/n): ")
            if proseguir.lower() != 's':
                print("Obrigado por usar a calculadora!")
                break
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

# Chamar a função da calculadora
calcular()
