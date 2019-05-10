#Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante.
#Escreva um programa que pergunta a situação do usuário (se é idoso, se é gestante, se é cadeirante ou nenhum destes)
#e diga se ele pode ter acesso a fila prioridade ou não.

print('1 - para voce que idoso')
print('2 - para voce que e gestante')
print('3 - para voe e cadeirante')
print('4 - nenhum destes')

prioridade = int(input('Digite seu numero de prioridade'))
if(prioridade == 1  or prioridade == 2 or  prioridade == 3 ):
 print('Voce tem direito a fila de prioridade')
else:
    print('Voce nao tem direito ,volte para a fila')