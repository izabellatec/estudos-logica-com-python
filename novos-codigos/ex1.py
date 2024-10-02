# 1. Soma de Números ÍmparesCrie um programa que peça um número inteiro positivo n e calcule a soma de todos os números ímpares de 1 até n.

#Exemplo:Para n = 10, a soma dos números ímpares de 1 a 10 é 1 + 3 + 5 + 7 + 9 = 25.
#Dica: Use um laço for para iterar e uma estrutura condicional if para verificar se o número é ímpar.

n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        soma += i

print(f"A soma dos números ímpares de 1 a {n} é: {soma}")

#Crie um programa que solicite um número inteiro do usuário e exiba a tabuada de multiplicação desse número de 1 a 10.

#Exemplo:Para n = 5, a saída deve ser:5 x 1 = 55 x 2 = 10, 5 x 10 = 50
n = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

