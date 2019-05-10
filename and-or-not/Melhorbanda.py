#criar um script que pergunta qual a melhor banda , para o usuário.

#Se ele não digitar 'rush', chama o usuário de herege.
#Se digitar, ok, parabeniza. Veja:

banda = input('Qual melhor banda ? ')

if not banda=='nirvana':
    print('Herege!')
else:
    print('Correto, é a Nirvana!')