# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa de quiz simples com perguntas de conhecimentos gerais.


import os

os.system('cls' if os.name == 'nt' else 'clear')

perguntas = [['Quanto é 2 + 2?', 4],
            ['Qual linguagem estamos aprendendo?', 'Python'],
            ['Qual animal é famoso por rir?', 'Hiena'],
            ['Qual o nome do robot da série "Star Wars"?', 'R2-D2'],
            ['Qual é a capital da França?', 'Paris'],
            ['Quantos dias tem um ano bissexto?', 366],
            ]


print("Bem-vindo ao Quiz de Conhecimentos Gerais!")
print()
acertos = 0

for pergunta in perguntas:
    resposta = input(pergunta[0] + " ")
    if resposta.lower() == pergunta[1]:
        acertos += 1
        print("Resposta correta!")
    else:
        print(f"Resposta incorreta! A resposta certa é: {pergunta[1]}")
    print()
print(f"Você acertou {acertos} de {len(perguntas)} perguntas.")