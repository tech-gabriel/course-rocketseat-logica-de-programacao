# Nível 2  - Escrevendo seu primeiro programa
# Módulo   - Do pensamento lógico à prática com Python
# Conteúdo - Controlando o fluxo do execução
# Aula     - 7 - Estruturas condicionais simples e compostas


"""Teste condicional para verificar se a pessoa é maior ou menor de idade, utilizando IF e ELSE."""
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Bem vindo ao sistema de verificação de idade!")
idade = int(input("Por favor, insira sua idade: "))

if int( idade) >= 18:
    print()
    print("Você é maior de idade.")
else:
    print()
    print("Você é menor de idade.")
print()
print("Obrigado por usar o sistema de verificação de idade!") 
print("--------------------------------")

"""Teste condicional para verificar a situação do aluno com base na nota, utilizando do ELIF."""
print("Bem vindo ao sistema de verificação de notas!")
print()
nota = int(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado!")
elif nota < 5:
    print("Reprovado!")
else:
    print("Recuperação!")
print("Obrigado por usar o sistema de verificação de notas!") 
