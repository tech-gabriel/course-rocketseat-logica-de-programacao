# --- 1. PREPARAÇÃO DO AMBIENTE ---

# "importar" é como pedir uma "caixa de ferramentas" extra para o Python.
# A caixa 'os' (Operating System) nos permite interagir com o sistema operacional.
import os

# Aqui, usamos uma ferramenta da caixa 'os' para limpar o terminal.
# 'os.name' verifica se o sistema é Windows ('nt').
# Se for Windows, executa 'cls'. Se não (Linux/Mac), executa 'clear'.
# Isso garante que o jogo comece com uma tela limpa.
os.system('cls' if os.name == 'nt' else 'clear')


# --- 2. CONFIGURAÇÃO INICIAL DO JOGO ---

# Criamos o nosso tabuleiro.
# É uma "lista de listas" (ou uma matriz) para representar um grid 3x3.
# Pense nisso como 3 linhas, e cada linha tem 3 colunas.
# Inicia tudo com ' ' (espaços vazios).
tabuleiro = [
    [' ', ' ', ' '],  # Linha 0 (índice 0)
    [' ', ' ', ' '],  # Linha 1 (índice 1)
    [' ', ' ', ' ']   # Linha 2 (índice 2)
]

# Definimos a "resposta" do jogo.
# O tesouro está escondido na Linha 1, Coluna 2.
# Em Python, a contagem sempre começa do 0.
linha_tesouro = 1
coluna_tesouro = 2


# --- 3. FUNÇÃO PARA MOSTRAR O JOGO ---

# 'def' define uma "função". Uma função é um bloco de código que podemos chamar (executar) várias vezes pelo seu nome.
# Esta função serve para "desenhar" o tabuleiro no terminal.
def exibir_tabuleiro():
    # Isso é um "loop" (laço de repetição).
    # Para cada 'linha' dentro da nossa lista 'tabuleiro'...
    for linha in tabuleiro:
        #...imprimimos a linha.
        # 'join' é um método que junta os itens da lista (' ', ' ', ' ') usando um '|' como separador.
        print('|'.join(linha))
        
        # Imprime uma linha pontilhada para separar as linhas do tabuleiro.
        print('-' * 5) # ('-' multiplicado por 5 = '-----')


# --- 4. INÍCIO DO JOGO E REGRAS ---

# Definimos uma variável para guardar o número de chances do jogador.
tentativas = 5

# Imprime as mensagens de boas-vindas e as regras para o jogador.
print("Bem-vindo ao jogo do Tesouro!")
print(f"Você tem {tentativas} tentativas para encontrar o tesouro (💎) escondido no tabuleiro 3x3.")
print("As linhas e colunas são numeradas de 0 a 2.")
print("Exemplo de entrada: linha 0, coluna 1")
print() # Imprime uma linha em branco para espaçamento.


# --- 5. O LOOP PRINCIPAL DO JOGO ---

# Este é o "loop" principal do jogo.
# 'range(tentativas)' cria uma sequência de números de 0 a 4 (total de 5 números).
# O código dentro deste 'for' vai se repetir 5 vezes (uma para cada tentativa).
# A variável 'i' vai valer 0, depois 1, 2, 3, e 4.
for i in range(tentativas):
    # Imprime qual tentativa estamos.
    # Usamos 'i + 1' porque 'i' começa em 0, mas queremos mostrar "Tentativa 1".
    # O '\n' significa "pular uma linha" antes de imprimir.
    print(f'\nTentativa {i+1} de {tentativas}')

    # 'input()' pausa o programa e pede para o usuário digitar algo.
    # 'int()' converte o texto que o usuário digitou (string) em um número inteiro.
    linha = int(input("Digite a linha (0, 1 ou 2): "))
    coluna = int(input('Digite a coluna (0, 1 ou 2): '))

    # --- 6. VERIFICAÇÕES DA JOGADA ---

    # Verifica se o usuário digitou um número fora do tabuleiro (menor que 0 ou maior que 2).
    # 'or' significa que se UMA das condições for verdadeira, ele entra no 'if'.
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        print('❌ Posição inválida! Tente valores entre 0 e 2.')
        # 'continue' é uma palavra-chave especial.
        # Ela "pula" o resto do código desta volta do loop e vai direto
        # para a próxima tentativa (o próximo 'i').
        continue

    # Se a posição for válida, verificamos se é a posição do tesouro.
    # '==' significa "é igual a?"
    # 'and' significa que AMBAS as condições devem ser verdadeiras.
    if linha == linha_tesouro and coluna == coluna_tesouro:
        # Se acertou:
        # 1. Coloca o '💎' na posição exata do tabuleiro.
        #    tabuleiro[linha] acessa a lista da linha.
        #    [coluna] acessa o item dentro daquela lista.
        tabuleiro[linha][coluna] = '💎'
        # 2. Mostra o tabuleiro com o tesouro.
        exibir_tabuleiro()
        # 3. Imprime a mensagem de vitória.
        print('🎉 Parabéns! Você encontrou o tesouro!')
        # 4. 'break' é outra palavra-chave especial.
        #    Ela "quebra" o loop 'for' e sai dele imediatamente.
        #    O jogo acaba aqui, pois o jogador venceu.
        break
    
    # 'else' (se não): Se a condição do 'if' de cima (acertar o tesouro) for FALSA.
    else:
        # O jogador errou. Vamos verificar se ele já tentou aqui.
        if tabuleiro[linha][coluna] == '❌':
            print('Você já tentou essa posição. Tente outra.')
        # Se não for uma posição repetida...
        else:
            # 1. Marca a posição no tabuleiro com '❌' para o jogador saber que já tentou ali.
            tabuleiro[linha][coluna] = '❌'
            # 2. Imprime a mensagem de erro.
            print('Nada aqui... Tente novamente!')
        
        # Mostra o tabuleiro atualizado com o '❌' (ou a msg de repetido).
        exibir_tabuleiro()


# --- 7. FIM DO JOGO (SE O LOOP TERMINAR) ---

# Este 'else' é especial! Ele pertence ao 'for' lá de cima.
# O código dentro deste 'else' SÓ executa se o loop 'for' terminar
# "naturalmente" (ou seja, se as 5 tentativas acabarem)
# e o 'break' (de vitória) NUNCA for chamado.
else:
    print('\n😞 Suas tentativas acabaram!')
    # Mostra onde o tesouro estava.
    tabuleiro[linha_tesouro][coluna_tesouro] = '💎'
    print('O tesouro estava aqui: ')
    exibir_tabuleiro()