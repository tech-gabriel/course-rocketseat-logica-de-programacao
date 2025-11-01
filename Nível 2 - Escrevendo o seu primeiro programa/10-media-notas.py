# Nível 2   - Escrevendo seu primeiro programa
# Módulo    - Do pensamento lógico à prática com Python
# Conteúdo  - Controlando o fluxo do execução
# Aula      - 10 - Arrays, armazenando vários dados em listas


"""Calculando a média das notas de um aluno"""
notas = [9, 9.5, 10, 9.8]

# Somando todas as notas
media = 0
for nota in notas:
    media += nota

# Dividindo a soma das notas pelo número de notas
media /= 4

# Exibindo a média das notas
print(f'A média das notas é {media}')