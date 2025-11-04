# Desafio prático
# Nível 2 - Escrevendo seu primeiro programa
# Objetivo: Vamos criar uma história engraçada! Peça ao usuário para fornecer um lugar, uma pessoa famosa, um objeto, uma cor, um verbo e um número. Em seguida, gere uma história divertida usando essas informações.


import os

os.system('cls' if os.name == 'nt' else 'clear')

print('Vamos criar uma história engraçada!')

lugar = input('Digite um lugar: ')
pessoa = input('Digite o nome de uma pessoa famosa: ')
objeto = input('Digite um objeto: ')
cor = input('Digite uma cor: ')
verbo = input('Digite um verbo: ')
numero = input('Digite um número: ')

print('\nAqui está a sua história:\n')
print(f'Um dia, no(a) {lugar}, encontrei o(a) {pessoa} segurando um(a) {objeto} {cor}.')
print(f'Ele(a) começou a {verbo} sem parar, e isso durou por {numero} horas!')