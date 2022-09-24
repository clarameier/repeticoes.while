#imports
from random import randint
from time import sleep

#game
pc = randint(0,10)
sleep(1.5)
print('Sou uma inteligência artificial e acabei de pensar em um número entre 0 e 10...')
sleep(1.5)  
print('Será que você é capaz de descobrir qual foi o número pensado por mim?')
sleep(1.5)
acertou = False
tentativa = 0
while not acertou:
    sleep(1.5)
    jogo = int(input('Faça sua tentativa: '))
    tentativa += 1
    if jogo == pc:
        acertou = True
    else:
        if jogo < pc:
            print('Dica, é um número maior, tente novamente.')
        elif jogo > pc:
            print('Dica, é um número menor, tente novamente.')
sleep(1.5)
print('Parece que você me venceu... parabéns você acertou com {} tentativas!'.format(tentativa))