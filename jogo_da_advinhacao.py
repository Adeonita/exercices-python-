numero = 40
tentativas = 3

print("\n\nBem vindo ao jogo da advinhação!!\n\n")
nome = input("Qual o seu nome? ")
apelido = input("E qual seu apelido? ")
print("\nEntão {}, no jogo da advinhação e você tem 3 tentativas para advinhar o número da sorte, que fica entre 0 (Zero) e 100 (Cem) \nBoa sorte, Vamos lá!!! ".format(apelido))


while(tentativas > 0):
    valor_lido = input('\n\nDigite um número: ')
    chute = int(valor_lido)

    acertou = chute == numero
    maior = chute > numero
    menor = chute < numero

    if (acertou):
        print("Parabens " + nome + " Você Acertou!!" )
        break
    elif(menor):
        if(tentativas == 1 and chute == numero):
            print("Parabens " + nome + " Você Acertou!!" ) 
        elif(tentativas == 1 and chute != numero):
            print("\nQue pena, suas chances acabaram e o jogo também :( ")
        else:
            print("Quase, tente um número maior")
    elif(maior):
        if(tentativas == 1 and chute == numero):
            print("Parabens " + nome + " Você Acertou!!" ) 
        elif(tentativas == 1 and chute != numero):
            print("\nQue pena, suas chances acabaram e o jogo também :( ")
        else:
            print("Quase, tente um numero menor")

    tentativas = tentativas -1
    if(tentativas == 1 ):
        print("\nÚ L T I M A      C H A N C E")

