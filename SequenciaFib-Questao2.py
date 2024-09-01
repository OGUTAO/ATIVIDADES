#Questão 2: 
#Python

def pertencea(n):

    a, b = 0, 1 

    while b < n:

        a, b = b, a + b

    return b == n or n == 0

numero = int(input("Informe um número: "))

if pertencea(numero):

    print(f"O número {numero} pertence à sequência de Fibonacci.")

else:

    print(f"O número {numero} não pertence à sequência de Fibonacci.")
