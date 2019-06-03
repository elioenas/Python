"""Declaração de quebra
No Python, a breakinstrução fornece a oportunidade de sair de um loop quando uma condição externa é acionada. Você colocará a breakinstrução dentro do bloco de código sob sua instrução de loop, geralmente após uma instrução condicionalif .

Vamos ver um exemplo que usa a breakinstrução em um forloop:"""

number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      break    # break here

   print('Number is ' + str(number))

print('Out of loop')

"""Neste pequeno programa, a variável numberé inicializada em 0. Em seguida, uma forinstrução constrói o loop, desde que a variável numberseja menor que 10.

Dentro do forloop, o número aumenta incrementalmente em 1 com cada passagem devido à linha number = number + 1.

Então, há uma ifdeclaração que apresenta a condição de que , se a variável numberé equivalente ao inteiro 5, em seguida, o loop vai quebrar.

Dentro do loop também é uma print()instrução que será executada a cada iteração do forloop até que o loop seja interrompido, já que é após a breakinstrução.

Para ver quando estamos fora do loop, incluímos uma print()instrução final fora do forloop.

Quando executamos esse código, nossa saída será a seguinte:"""

"""Output
Number is 1
Number is 2
Number is 3
Number is 4
Out of loop"""

"""Isso mostra que, uma vez que o inteiro numberé avaliado como equivalente a 5, o loop é interrompido, pois o programa é instruído a fazê-lo com a breakinstrução.

A breakinstrução faz com que um programa saia de um loop.

Continue a Declaração
A continueinstrução lhe dá a opção de pular a parte de um loop onde uma condição externa é acionada, mas continuar completando o restante do loop. Ou seja, a iteração atual do loop será interrompida, mas o programa retornará ao início do loop.

A continueinstrução estará dentro do bloco de código sob a instrução loop, geralmente após uma ifinstrução condicional .

Usando o mesmo forprograma de loop da seção Break Statement acima, usaremos uma continueinstrução em vez de uma breakinstrução:"""

number = 0

for number in range(10):
   number = number + 1

   if number == 5:
      continue    # continue here

   print('Number is ' + str(number))

print('Out of loop')
"""A diferença em usar a continuedeclaração em vez de uma breakdeclaração é que nosso código continuará 
apesar da interrupção quando a variável numberé avaliada como equivalente a 5. Vamos ver nossa saída:"""

"""Output
Number is 1
Number is 2
Number is 3
Number is 4
Number is 6
Number is 7
Number is 8
Number is 9
Number is 10
Out of loop"""

"""Aqui vemos que a linha Number is 5nunca ocorre na saída, mas o loop continua depois desse ponto para imprimir linhas para os números 6-10 antes de sair do loop.

Você pode usar a continueinstrução para evitar código condicional profundamente aninhado ou otimizar um loop, eliminando casos de ocorrência freqüente que você gostaria de rejeitar.

A continueinstrução faz com que um programa pule alguns fatores que aparecem em um loop, mas continue pelo restante do loop."""