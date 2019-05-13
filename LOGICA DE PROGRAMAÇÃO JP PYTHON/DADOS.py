# Meu primeiro programa

from random import randint  # importa a função de gerar números aleatórios

print("Jogos dos dados: ")

dado1 = randint(1, 6)   # gera um número aleatório entre 1 e 6
print("Dado 1: ", dado1)

dado2 = randint(1, 6)   # gera um número aleatório entre 1 e 6
print("Dado 2: ", dado2)


dado3 = randint(1, 6)   # gera um número aleatório entre 1 e 6
print("Dado 3: ", dado3)


dado4 = randint(1, 6)   # gera um número aleatório entre 1 e 6
print("Dado 4: ", dado4)


jogador1 = dado1 + dado2
jogador2 = dado3 + dado4

print('jogador 1: ', jogador1)
print('jogador 2: ', jogador2)

if jogador1 > jogador2:
    print("jogador um venceu!")
else:
    if jogador2 > jogador1:
        print("jogador2 venceu!")
    else:
        print("Empate!")
