# Nível 2   - Escrevendo seu primeiro programa
# Módulo    - Do pensamento lógico à prática com Python
# Conteúdo  - Controlando o fluxo do execução
# Aula      - 13, 14 e 15 - Criando um jogo da velha


"""Implementação de um jogo da velha simples para dois jogadores."""

# Definição do tabuleiro e funções para exibir o tabuleiro e fazer jogadas.
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

# Jogador atual
jogador = "X"

def exibeTabuleiro():
    """Exibe o estado atual do tabuleiro."""
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

def jogada(linha, coluna):
    """Realiza uma jogada no tabuleiro."""
    if ( # Validação da jogada, garantindo que a posição está dentro dos limites e vazia.
        not 0 <= linha <= 2 or 
        not 0 <= coluna <= 2 or 
        tabuleiro[linha][coluna] != " "
    ):
        print('Jogada inválida!')
        return jogador
    tabuleiro[linha][coluna] = jogador
    return "O" if jogador == "X" else "X"

def temGanhador():
    """Verifica se há um ganhador no jogo."""

    # Verificação das linhas para um ganhador
    for linha in range(3):
        if (
            tabuleiro[linha][0] != ' ' and
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            tabuleiro[linha][0] == tabuleiro[linha][2]    
        ):
            print(f"{tabuleiro[linha][0]} GANHOU!!!")
            return True
    
    # Verificação das colunas para um ganhador
    for coluna in range(3):
        if (
            tabuleiro[0][coluna] != ' ' and
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            tabuleiro[0][coluna] == tabuleiro[2][coluna]    
        ):
            print(f"{tabuleiro[0][coluna]} GANHOU!!!")
            return True
    
    # Verificação das diagonais para um ganhador
    if (
        tabuleiro[1][1] != ' ' and
        (
            (
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            ) or 
            (
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )   
    ):
        print(f"{tabuleiro[1][1]} GANHOU!!!")
        return True
    
    return False

def temEmpate():
    """Verifica se o jogo terminou em empate."""
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == ' ':
                return False
    print("EMPATE!!!")
    return True

# Loop principal do jogo
while True:
    print(f"Vez do jogador {jogador}")
    
    try:    # try-except para tratar entradas inválidas
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))
        jogador = jogada(linha, coluna)
    
    except ValueError:  # except para capturar erros de entrada.
        print("Entrada inválida! Por favor, insira números inteiros entre 0 e 2.")
    
    except IndexError: # except para capturar erros de índice fora do intervalo.
        print("Posição inválida! Por favor, insira números entre 0 e 2.")
    
    exibeTabuleiro()
    if temGanhador() or temEmpate():
        break