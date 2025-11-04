# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Criar um jogo simples onde o usuário deve encontrar um "tesouro" escondido em um tabuleiro 3x3. O usuário terá 5 tentativas para adivinhar a posição correta do tesouro.


import os

os.system('cls' if os.name == 'nt' else 'clear')

tabuleiro = [[' ', ' ', ' '],   # Linha 0
            [' ', ' ', ' '],    # Linha 1
            [' ', ' ', ' ']     # Linha 2
            ]

linha_tesouro = 1
coluna_tesouro = 2

def exibir_tabuleiro():
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 5)

tentativas = 5

print("Bem-vindo ao jogo do Tesouro!")
print("Você tem 5 tentativas para encontrar o tesouro (💎) escondido no tabuleiro 3x3.")
print("As linhas e colunas são numeradas de 0 a 2.")
print("Exemplo de entrada: linha 0, coluna 1")
print()

for i in range(tentativas):
    print(f'\nTentativa {i+1} de {tentativas}')

    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input('Digite a coluna (0, 1 ou 2): '))

    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('❌ Posição inválida! Tente valores entre 0 e 2.')
        continue

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = '💎'
        exibir_tabuleiro()
        print('🎉 Parabéns! Você encontrou o tesouro!')
        break
    else:
        if tabuleiro[linha][coluna] == '❌':
            print('Você já tentou essa posição. Tente outra.')
        else:
            tabuleiro[linha][coluna] = '❌'
            exibir_tabuleiro()
            print('Nada aqui... Tente novamente!')
        exibir_tabuleiro()

else:
    print('\n😞 Suas tentativas acabaram!')
    tabuleiro[linha_tesouro][coluna_tesouro] = '💎'
    print('O tesouro estava aqui: ')
    exibir_tabuleiro()