# Nível 2   - Escrevendo seu primeiro programa
# Módulo    - Do pensamento lógico à prática com Python
# Conteúdo  - Controlando o fluxo do execução
# Aula      - 12 - Reutilizando códigos com funções


"""Funções em Python"""
# Funções permitem reutilizar blocos de código e melhorar a legibilidade.

# A palavra "def" define uma função
def ola_mundo():
    """Exibe a mensagem 'Olá, Mundo!' na tela."""
    print("Olá, Mundo!")


def ola_usuario(nome):
    """Exibe uma mensagem personalizada para o usuário."""
    print(f"Olá, {nome}! Seja bem-vindo!")

def dobro(numero):
    """Retorna o dobro do número fornecido."""
    return numero * 2

def multiplica(a, b):
    """Retorna o produto de dois números."""
    return a * b

def variaveis_locais():
    """Exemplo de variáveis locais dentro de uma função."""
    x = 10
    y = 20
    print(f"Soma dentro da função: {x + y}")

z = 0  # Variável global
def variaveis_globais():
    """Exemplo de uso de variáveis globais."""
    print(f"Valor global dentro da função: {z}")

# Chamando as funções definidas
ola_mundo()
print("------------------------------------------")

ola_usuario("Alice")
print("------------------------------------------")

print(f"O dobro de 5 é {dobro(5)}")
print("------------------------------------------")

print(f"O produto de 4 e 6 é {multiplica(4, 6)}")
print("------------------------------------------")

variaveis_locais()
print("Note que variáveis locais não são acessíveis fora da função")
print("------------------------------------------")

variaveis_globais()
print("------------------------------------------")