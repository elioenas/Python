"""Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato."""

"""criar a variavel"""

eleitores = int(input('numero de eleitores:'))

votos =[]
"""um for onde o ira contar numero de eleitores e  determinar quantos votos tera"""
for i in range(eleitores):
    voto = votos.append(int(input('Digite o numero do seu candidato [1,2,3] :')))

print('')
print('Quantidade de eleitores',eleitores)
print('O candidato1 teve um total de ',votos.count(1), 'votos')
print('O candidato2 teve um total de ',votos.count(2), 'votos')
print('O candidato3 teve um total de ',votos.count(3), 'votos')
