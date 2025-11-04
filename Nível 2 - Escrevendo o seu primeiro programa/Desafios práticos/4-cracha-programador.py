# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa que gere um crachá de evento tech. Peça ao usuário seu nome, idade, linguagem de programação favorita e um emoji que o represente. No final, exiba o crachá formatado com essas informações.


import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Bem-vindo ao gerador de crachás de evento tech!")
print()
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
linguagem = input("Digite sua linguagem de programação favorita: ")
emoji = input("Digite um emoji que te representa: ")

print()
print("Aqui está o seu crachá de evento tech:")
print("-----------------------------------")
print('👨‍💻 Crachá:')
print('Nome: ', nome)
print('Idade: ', idade)
print('Linguagem Favorita: ', linguagem)
print('Emoji: ', emoji)
print("-----------------------------------")