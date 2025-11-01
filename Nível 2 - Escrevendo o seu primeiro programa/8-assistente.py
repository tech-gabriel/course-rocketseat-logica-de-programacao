# Nível 2   - Escrevendo seu primeiro programa
# Módulo    - Do pensamento lógico à prática com Python
# Conteúdo  - Controlando o fluxo do execução
# Aula      - 8 - Estruturas condicionais aninhadas

"""Teste condicional para verificar se a pessoa é maior ou menor de idade, utilizando MATCH CASE."""
import os

print("Olá, eu sou seu assistente virtual!")
print("O que você gostaria de fazer hoje?")
print()
print("1. Verificar idade")
print("2. Verificar nota")
print("3. Ouvir uma piada")
print("4. Sair")
print()

comando = input("Digite um comando: ").lower()

# Usando o MATCH CASE para selecionar a ação com base no comando do usuário.
match comando:
    case "1" | "verificar idade":
        print()
        idade = int(input("Por favor, insira sua idade:"))
        print()
        os.system('cls' if os.name == 'nt' else 'clear')
        if int( idade) >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")
        print()
        print("Obrigado por usar o sistema de verificação de idade!")
    
    case "2" | "verificar nota":
        print()
        nota = int(input("Digite a nota do aluno: "))
        if nota >= 7:
            print("Aprovado!")
        elif nota < 5:
            print("Reprovado!")
        else:
            print("Recuperação!")
    
    case "3" | "ouvir uma piada":
        print("Por que o livro de matemática se suicidou? Porque ele tinha muitos problemas.")
    
    case "4" |"sair":
        print("Obrigado por usar o assistente virtual. Até mais!")

    case _:
        print("Desculpe, comando não reconhecido.")