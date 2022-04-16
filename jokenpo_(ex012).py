from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
player = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(0.75)
print('PO!!!')
sleep(0.5)
print('-='*15)
print('Computador escolheu {}.'.format(itens[bot]))
print('Jogador escolheu: {}.'.format(itens[player]))
print('-='*15)

if bot == 0: #bot jogou Pedra
    if player == 0:
        print('EMPATOU!')
    elif player == 1:
        print('PARABÉNS! Você venceu')
    elif player == 2:
        print('O robô venceu!')
    else:
        print('JOGADA INVÁLIDA')
elif bot == 1: #bot jogou Papel
    if player == 1:
        print('EMPATOU!')
    elif player == 2:
        print('PARABÉNS! Você venceu')
    elif player == 0:
        print('O robô venceu!')
    else:
        print('JOGADA INVÁLIDA')
elif bot == 2:#bot jogou Tesoura
    if player == 2:
        print('EMPATOU!')
    elif player == 0:
        print('PARABÉNS! Você venceu')
    elif player == 1:
        print('O robô venceu!')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA!')