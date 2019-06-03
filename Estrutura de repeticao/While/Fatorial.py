print(' Calculadora fatorial ')
num1 = int(input('Informe o numero:'))

resultado = 1
count = 1

while count <= num1:
    resultado *= count
    count += 1
    print(num1, '!', '=', resultado)
