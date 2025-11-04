# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Crie um programa que funcione como um "oráculo da sabedoria". O usuário pode perguntar sobre conceitos básicos de programação (como funções, loops, variáveis, listas) e o programa deve responder com uma explicação simples sobre o tópico escolhido.


import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Bem-vindo ao Oráculo da Sabedoria!")
print()
pergunta = input("Você quer saber sobre (funções, loops, variáveis, listas)? ")
print()

match pergunta.lower():
    case 'funções' | 'funcoes' | 'função' | 'funcao':
        print("Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas ajudam a organizar o código e facilitar a manutenção.")
    case 'loops' | 'loop' | 'repetições':
        print("Loops são estruturas que permitem repetir um bloco de código várias vezes até que uma condição seja atendida. Exemplos incluem 'for' e 'while'.")
    case 'variáveis' | 'variaveis' | 'variável' | 'variavel':
        print("Variáveis são espaços na memória que armazenam dados. Elas podem conter diferentes tipos de valores, como números, texto ou listas.")
    case 'listas' | 'lista' | 'arrays':
        print("Listas são coleções ordenadas de itens que podem ser de diferentes tipos. Elas permitem armazenar múltiplos valores em uma única variável e oferecem várias operações para manipulação dos dados.")
    case _:
        print("Desculpe, não tenho informações sobre esse tópico no momento. Tente perguntar sobre funções, loops, variáveis ou listas.")