"""
Um numero triangular é calculado pela fórmula
triangular = n *(n+1)//2
Sendo n o índice desse número triangular
Escreva um programa que imprima os numeros triangulares com indices
múltiplos de 5 entre 5 e 50"""

n = int(input('Informe o numero:'))

for n in range(5,51,5):
    triangular = n * (n + 1) // 2
    print("%i número triangular = %i" % (n, triangular))
