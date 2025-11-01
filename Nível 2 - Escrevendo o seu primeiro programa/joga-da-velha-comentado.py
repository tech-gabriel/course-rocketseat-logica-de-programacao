# A variável 'tabuleiro' é a nossa estrutura de dados principal.
# É uma "lista de listas" (uma matriz 3x3) que representa o grid do jogo.
# Cada ' ' (espaço) representa uma casa vazia.
tabuleiro = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

# Jogador atual
# Esta variável global armazena de quem é a vez de jogar. O jogo começa com o "X".
jogador = "X"


# 'def' define uma função. Esta se chama 'exibeTabuleiro'.
# Ela não precisa de nenhuma informação extra (sem parâmetros) para funcionar.
def exibeTabuleiro():
    """Exibe o estado atual do tabuleiro."""
    
    # 'for linha in tabuleiro:' itera (passa por) cada item da lista 'tabuleiro'.
    # Como 'tabuleiro' é uma lista de listas, 'linha' será cada uma das listas internas.
    for linha in tabuleiro:
        # 'print("|".join(linha))' é um truque para formatar a saída.
        # '.join()' junta todos os itens da lista 'linha' usando o caractere "|" como separador.
        print("|".join(linha))
        
        # Imprime uma linha "----" para separar visualmente as linhas do tabuleiro.
        print("-" * 5)


# Esta função define o que acontece quando um jogador tenta fazer uma 'jogada'.
# Ela precisa saber a 'linha' e a 'coluna' que o jogador escolheu.
def jogada(linha, coluna):
    """Realiza uma jogada no tabuleiro."""
    
    # O 'if' verifica múltiplas condições usando 'or' (ou).
    if ( # Validação da jogada, garantindo que a posição está dentro dos limites e vazia.
        
        # 'not 0 <= linha <= 2': Verifica se a linha NÃO está entre 0 e 2.
        not 0 <= linha <= 2 or 
        
        # 'not 0 <= coluna <= 2': Verifica se a coluna NÃO está entre 0 e 2.
        not 0 <= coluna <= 2 or 
        
        # 'tabuleiro[linha][coluna] != " "': Verifica se a casa escolhida NÃO está vazia.
        tabuleiro[linha][coluna] != " "
    ):
        # Se QUALQUER uma das condições acima for Verdadeira, a jogada é inválida.
        # A função retorna o 'jogador' atual.
        print('Jogada inválida!')
        return jogador
    
    # Se o 'if' de validação for Falso (ou seja, a jogada é VÁLIDA):
    # A casa do tabuleiro (ex: tabuleiro[1][2]) recebe o símbolo do jogador atual (ex: "X").
    tabuleiro[linha][coluna] = jogador
    
    # Esta é a lógica de TROCA DE JOGADOR.
    # É um "operador ternário" (um 'if' em uma linha só).
    # Lê-se: "Retorne 'O' SE o jogador for 'X', SENÃO (else) retorne 'X'."
    # O valor retornado ('O' ou 'X') será usado para atualizar a variável 'jogador' no loop principal.
    return "O" if jogador == "X" else "X"


def temGanhador():
    """Verifica se há um ganhador no jogo."""

    # Verificação das linhas para um ganhador
    # 'for linha in range(3)' vai executar o bloco de código 3 vezes (com 'linha' valendo 0, depois 1, depois 2).
    for linha in range(3):
        if (
            # 1. A casa inicial da linha (coluna 0) não pode estar vazia.
            tabuleiro[linha][0] != ' ' and
            # 2. A casa 0 (ex: [0][0]) tem que ser igual à casa 1 (ex: [0][1]).
            tabuleiro[linha][0] == tabuleiro[linha][1] and
            # 3. A casa 0 (ex: [0][0]) tem que ser igual à casa 2 (ex: [0][2]).
            tabuleiro[linha][0] == tabuleiro[linha][2]    
            # Se as 3 condições são Verdadeiras, temos um ganhador na linha!
        ):
            print(f"{tabuleiro[linha][0]} GANHOU!!!") # Anuncia o ganhador (ex: "X GANHOU!!!")
            return True # Retorna Verdadeiro, pois o jogo acabou e tem um ganhador.
    
    # Verificação das colunas para um ganhador
    # A lógica é idêntica à das linhas, mas fixamos a 'coluna' e mudamos a 'linha' na verificação.
    for coluna in range(3):
        if (
            # 1. A casa do topo da coluna (linha 0) não pode estar vazia.
            tabuleiro[0][coluna] != ' ' and
            # 2. A casa [0][coluna] tem que ser igual à [1][coluna].
            tabuleiro[0][coluna] == tabuleiro[1][coluna] and
            # 3. A casa [0][coluna] tem que ser igual à [2][coluna].
            tabuleiro[0][coluna] == tabuleiro[2][coluna]    
        ):
            print(f"{tabuleiro[0][coluna]} GANHOU!!!")
            return True # Encontramos um ganhador na coluna.
    
    # Verificação das diagonais para um ganhador
    if (
        # Otimização: Ambas as diagonais passam pelo centro (1,1).
        # Se o centro estiver vazio, é impossível ter uma vitória na diagonal.
        tabuleiro[1][1] != ' ' and
        (
            (
                # Diagonal Principal (canto superior esquerdo para inferior direito)
                # Verifica se [0][0] == [1][1] == [2][2]
                tabuleiro[0][0] == tabuleiro[1][1] and
                tabuleiro[0][0] == tabuleiro[2][2]
            ) or # 'OU' (basta uma das diagonais ser verdadeira)
            (
                # Diagonal Secundária (canto superior direito para inferior esquerdo)
                # Verifica se [0][2] == [1][1] == [2][0]
                tabuleiro[0][2] == tabuleiro[1][1] and
                tabuleiro[1][1] == tabuleiro[2][0]
            )
        )   
    ):
        print(f"{tabuleiro[1][1]} GANHOU!!!") # Anuncia o ganhador (o símbolo do meio).
        return True # Encontramos um ganhador na diagonal.
    
    # Se a função chegou até aqui, significa que nenhuma das verificações (linhas, colunas, diagonais) encontrou um ganhador.
    return False # Retorna Falso, indicando que NINGUÉM ganhou *nesta rodada*.


def temEmpate():
    """Verifica se o jogo terminou em empate."""
    # Esta função só deve ser chamada DEPOIS de 'temGanhador()'.
    # Ela assume que não há ganhador e apenas verifica se o tabuleiro está cheio.
    
    # 'for' aninhado: Para cada linha...
    for linha in range(3):
        # ...vamos verificar cada coluna.
        for coluna in range(3):
            # Se a casa [linha][coluna] estiver vazia (' ')...
            if tabuleiro[linha][coluna] == ' ':
                # ...significa que o jogo ainda não acabou (ainda há jogadas possíveis).
                return False # Retorna Falso, indicando que NÃO HÁ EMPATE.
    
    # Se o código saiu dos dois loops 'for', significa que ele verificou
    # todas as 9 casas e NÃO encontrou NENHUMA casa vazia.
    print("EMPATE!!!") # O tabuleiro está cheio e ninguém ganhou.
    return True # Retorna Verdadeiro, indicando que HÁ EMPATE.


# Loop principal do jogo
# 'while True:' cria um "loop infinito". O código dentro dele
# ficará se repetindo para sempre, a menos que um comando 'break' seja executado.
while True:
    print(f"Vez do jogador {jogador}") # Informa de quem é a vez.
    
    # 'try...except' é um bloco para "Tratamento de Erros".
    # O Python vai TENTAR (try) executar o código abaixo.
    try:    # try-except para tratar entradas inválidas
        # 'input()' captura o que o usuário digita (sempre como um texto/string).
        # 'int()' tenta converter esse texto para um número inteiro.
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))
        
        # Esta é a linha principal que "joga o jogo".
        # 1. Chama a função 'jogada()' com as coordenadas.
        # 2. A função 'jogada()' faz a validação, atualiza o 'tabuleiro' (se for válida)
        #    e retorna o símbolo do PRÓXIMO jogador (ou do mesmo, se inválida).
        # 3. O valor retornado (ex: "O") é salvo DE VOLTA na variável 'jogador'.
        jogador = jogada(linha, coluna)
    
    # 'except ValueError:' (Exceção de Valor)
    # Se o 'int()' falhar (ex: usuário digitou "a" ou "dois"), o Python pula para cá.
    except ValueError:  # except para capturar erros de entrada.
        print("Entrada inválida! Por favor, insira números inteiros entre 0 e 2.")
    
    # 'except IndexError:' (Exceção de Índice)
    # Este erro aconteceria se tentássemos acessar 'tabuleiro[5][5]', por exemplo.
    # No nosso código, a própria função 'jogada' já valida os números antes
    # de tentar acessar o tabuleiro, então este 'except' é mais uma segurança.
    except IndexError: # except para capturar erros de índice fora do intervalo.
        print("Posição inválida! Por favor, insira números entre 0 e 2.")
    
    # Após cada tentativa de jogada (seja ela válida, inválida ou um erro),
    # o tabuleiro é exibido na tela para o usuário ver o estado atual.
    exibeTabuleiro()
    
    # Condição de término do jogo:
    # 1. O Python chama 'temGanhador()'. Se ela retornar 'True'...
    # 2. ...ou (or) o Python chama 'temEmpate()'. Se ela retornar 'True'...
    # ...o 'if' será verdadeiro.
    if temGanhador() or temEmpate():
        break # 'break' é o comando que "quebra" o 'while True' e encerra o loop.

# Fim do programa (O 'break' leva o código para cá).