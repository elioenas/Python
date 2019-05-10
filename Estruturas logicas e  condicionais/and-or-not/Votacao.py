#Para votar, você deve ter entre 18 anos e menos de 65 anos.
#Escreva um programa que pergunte sua idade e diga se você é obrigado a votar ou não.

#Temos dois testes:
#Testar se tem 18 anos ou mais
#Testar se tem 65 ou menos

idade = int(input('Informe sua idade:'))

if(idade >= 18 and idade <= 65):
      print('Voce e obbrigado a votar')
else:
    print('Voce nao e obrigado a votar')
