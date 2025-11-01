# Nível 2  - Escrevendo seu primeiro programa
# Módulo   - Do pensamento lógico à prática com Python
# Conteúdo - Controlando o fluxo do execução
# Aula     - 9 - Estruturas de repetição (loops) 

"""Programa para somar números de 1 a 10 usando loops"""
soma = 0
n = 1

# Usando loop "while" -> Utilizar while quando não se sabe exatamente quantas vezes o bloco de código será repetido
while n <= 10:
    soma = soma + n
    n = n + 1
    print(f"Soma parcial: {soma}")
    print(f"Próximo número a ser adicionado: {n}")
    print("-----")


# Usando loop "for" -> Utilizar for para repetir um bloco de código um número específico de vezes
for index in range(1, 11):
    soma = soma + index

print(f"A soma dos números de 1 a 10 é: {soma}")