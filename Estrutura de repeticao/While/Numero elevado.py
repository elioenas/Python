"""
Faca um programa que peca dois numeros,base e expoente,calcule e mostre o primeiro
numero elevado ao segundo numero. Nao utilize a funcao potencia da linguagem
3*4 =  3x3x3x3 = 81
"""

num1 = int(input('Informe o numero da base:'))
num2= int(input('Informe o numero do expoente:'))

cont = 0
resultado = 1
while(cont < num2):
 resultado = resultado * num1
 cont = cont + 1
 print(num1,'elevado',num2,'=',resultado)


