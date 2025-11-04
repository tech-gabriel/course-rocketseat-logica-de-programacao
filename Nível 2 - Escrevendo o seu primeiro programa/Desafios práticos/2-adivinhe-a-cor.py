# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa que permita ao usuário escolher uma cor entre vermelho, azul, verde e amarelo, e "adivinhe" a cor escolhida no final.


import os

os.system('cls' if os.name == 'nt' else 'clear')

print('Escolha uma cor e memorize-a.....')
print('🔴 Vermelho')
print('🔵 Azul')
print('🟢 Verde')
print('🟡 Amarelo')
input('Pressione Enter quando estiver pronto...')

os.system('cls' if os.name == 'nt' else 'clear')
print('Agora, feche os olhos e visualize a cor que você escolheu...')
input('Pressione Enter para continuar...')
print('Você pensou na cor... 🔵 Azul! ')
