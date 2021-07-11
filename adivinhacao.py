import random

def jogar():
    print('*********************************')
    print('Bem vindo ao jogo de adivinhação!')
    print('*********************************')

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    # rodada = 1

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Díficil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5


    # while(rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print('Tentativa {} de {}'. format(rodada, total_de_tentativas))

        str_chute = input("Digite um número entre 1 e 100: ")
        print('Você digitou ', str_chute)
        chute = int(str_chute)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print('Você acertou e fez {} pontos!'.format(pontos))
            break
        else:
            if(maior):
                print('O seu chute foi maior do que o número secreto\n')
            elif(menor):
                print('O seu chute foi menor do que o número secreto\n')
            
        # if(rodada == total_tentativas):
        #     print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        # rodada = rodada + 1
            
    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar()