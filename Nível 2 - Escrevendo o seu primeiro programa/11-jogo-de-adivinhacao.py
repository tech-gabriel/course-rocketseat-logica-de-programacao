# Nível 2   - Escrevendo seu primeiro programa
# Módulo    - Do pensamento lógico à prática com Python
# Conteúdo  - Controlando o fluxo do execução
# Aula      - 11 - Criando um jogo de adivinhação


"""Jogo de Adivinhação de Animais"""
import os

# Lista de perguntas e respostas
perguntas = [
        ["Seu animal gosta de bananas?", "macaco"],
        ["Seu animal é domesticado?", "cachorro"],
        ["Seu animal vive na água?", "peixe"],
        ["Seu animal tem penas?", "pássaro"],
        ["Seu animal é um réptil?", "cobra"]
        ]

# Loop principal do jogo
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Pense em um animal e eu tentarei adivinhar qual é.")
    print("Responda às perguntas com 's' para sim e 'n' para não.")
    print()

    # Variável para controlar se o animal foi adivinhado
    acertou = False

    # Loop pelas perguntas
    for pergunta in perguntas:
        resposta = input(f"{pergunta[0]} (s/n): ")
        if resposta.lower() == 's':
            print(f"Você pensou em {pergunta[1]}!")
            acertou = True
            break

    # Se não acertou, pede para o usuário ensinar um novo animal
    if not acertou:
        animal = input("Não consegui adivinhar seu animal. Qual animal você estava pensando? ")
        novapergunta = input(f"Qual pergunta eu poderia ter feito para adivinhar que você estava pensando em um {animal}? ")
        perguntas.append([novapergunta, animal])
        print("Obrigado por me ensinar algo novo!")

    # Pergunta se o usuário quer jogar novamente
    jogar_novamente = input("Você quer jogar novamente? (s/n) ")
    # Se não quiser jogar novamente, sai do loop
    if jogar_novamente.lower() != "s":
        print ("Até a próxima!")
        break