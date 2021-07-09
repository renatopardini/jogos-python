print('*********************************')
print('Bem vindo ao jogo de adivinhação!')
print('*********************************')

numero_secreto = 28
total_de_tentativas = 3
rodada = 1

# while(rodada <= total_de_tentativas):
for rodada in range(1, 3):
    print('Tentativa {} de {}'. format(rodada, total_de_tentativas + 1))

    str_chute = input("Digite o seu número: ")
    print('Você digitou ', str_chute)
    chute = int(str_chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print('Você acertou!')
    else:
        if(maior):
            print('O seu chute foi maior do que o número secreto\n')
        elif(menor):
            print('O seu chute foi menor do que o número secreto\n')
    
    rodada = rodada + 1
        
print('Fim do jogo!')