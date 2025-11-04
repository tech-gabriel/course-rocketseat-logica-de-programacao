# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa que permita ao usuário adivinhar um número secreto entre 1 e 10. O programa deve continuar pedindo palpites até que o usuário acerte, e no final, mostrar quantas tentativas foram necessárias.


import os
os.system('cls' if os.name == 'nt' else 'clear')

numero_secreto = 7
tentativas = 0

print('Bem-vindo ao jogo do número secreto!')
while True:
    palpite = int(input('Adivinhe o número secreto (entre 1 e 10): '))
    tentativas += 1
    if palpite == numero_secreto:
        print(f'Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas.')
        break
    else:
        print('Número incorreto. Tente novamente!\n')