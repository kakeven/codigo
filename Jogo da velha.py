import os
import random
from colorama import Fore

Jogar_novamente = "s"
Jogadas = 0
quem_joga = random.randint(1,2)
Max_jogadas = 9
vit = True
velha = [
    [' ',' ', ' ', ' '],
    [' ',' ', ' ', ' '],
    [' ',' ', ' ', ' '],
    [' ',' ', ' ', ' '],
]

def tela():
    global velha
    
    print('    1   2   3')
    print('1:  ' + velha[1][1] + ' | ' + velha[1][2] + ' | ' + velha[1][3])
    print('   ---+---+---')
    print('2:  ' + velha[2][1] + ' | ' + velha[2][2] + ' | ' + velha[2][3])
    print('   ---+---+---')
    print('3:  ' + velha[3][1] + ' | ' + velha[3][2] + ' | ' + velha[3][3])
    print('Jogadas: ' + Fore.CYAN + str(Jogadas) + Fore.RESET)

def jogador():
    global Jogadas
    global quem_joga
    global Max_jogadas
    if quem_joga == 1 and Jogadas < Max_jogadas:
        linha = int(input('Digite a linha: '))
        coluna = int(input("Digite a coluna: "))
        
        while linha < 1 or linha > 3 or coluna < 1 or coluna > 3 or velha[linha][coluna] != " ":
            print('Linha e/ou coluna inválida ou já ocupada.')
            linha = int(input('Digite a linha: '))
            coluna = int(input("Digite a coluna: "))
        
        velha[linha][coluna] = 'X'
        quem_joga = 2
        Jogadas += 1

def CPU():
    global Jogadas
    global quem_joga
    global Max_jogadas
    if quem_joga == 2 and Jogadas < Max_jogadas:
        linha = random.randint(1, 3)
        coluna = random.randint(1, 3)
        while velha[linha][coluna] != " ":
            linha = random.randint(1, 3)
            coluna = random.randint(1, 3)
        
        velha[linha][coluna] = "O"
        quem_joga = 1
        Jogadas += 1

def ganhou():
    # Player 1 (X)
    for i in range(1, 4):
        if velha[i][1] == velha[i][2] == velha[i][3] == "X":  # Horizontal
            print("Player 1 Ganhou!")
            return True
        if velha[1][i] == velha[2][i] == velha[3][i] == "X":  # Vertical
            print("Player 1 Ganhou!")
            return True
    if velha[1][1] == velha[2][2] == velha[3][3] == "X" or velha[3][1] == velha[2][2] == velha[1][3] == "X":  # Diagonais
        print("Player 1 Ganhou!")
        return True
    
    # Player 2 (O)
    for i in range(1, 4):
        if velha[i][1] == velha[i][2] == velha[i][3] == "O":  # Horizontal
            print("Player 2 Ganhou!")
            return True
        if velha[1][i] == velha[2][i] == velha[3][i] == "O":  # Vertical
            print("Player 2 Ganhou!")
            return True
    if velha[1][1] == velha[2][2] == velha[3][3] == "O" or velha[3][1] == velha[2][2] == velha[1][3] == "O":  # Diagonais
        print("Player 2 Ganhou!")
        return True

    return False

def empate():
    if Jogadas == 9:
        print("Deu velha!")
        return True
    return False

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ").lower()
    return resposta == 's'

def reiniciar_jogo():
    global velha, Jogadas, quem_joga
    velha = [
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' '],
    ]
    Jogadas = 0
    quem_joga = random.randint(1, 2)

while True:
    tela()
    if ganhou() or empate():
        if not jogar_novamente():
            break
        else:
            reiniciar_jogo()
            continue
    jogador()
    CPU()
