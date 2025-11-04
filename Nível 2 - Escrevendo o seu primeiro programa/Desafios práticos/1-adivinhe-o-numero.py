# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa que "adivinhe" o número que o usuário está pensando entre 1 e 10.


import os

os.system('cls' if os.name == 'nt' else 'clear')

print('Pense em um número de 1 a 10.....')
input('Pressione Enter quando estiver pronto...')

os.system('cls' if os.name == 'nt' else 'clear')
print('Deixe-me adivinhar o número que você está pensando...')
input('Pressione Enter para revelar o número...')
print('O número que você está pensando é o 7!')