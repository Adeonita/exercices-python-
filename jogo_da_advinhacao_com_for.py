numero_da_sorte = 8
tentativas = 3
rodada = 1 

print("\n\nBem vindo ao jogo da Advinhação, você tem 3 chances para acertar um número de 0 (Zero) a 9 (Nove)")

for rodada in range( 1, tentativas + 1):
    if(rodada == 3):
        print("\n\nÚltima Rodada\n")

    print("\n\nRodada {} de {}". format(rodada, tentativas))

    chute = int(input("Digite um número: "))
    acertou = chute == numero_da_sorte
    foi_maior = chute > numero_da_sorte
    foi_menor = chute < numero_da_sorte

    if(acertou):
        print("\n\n***************Parabéns, você acertou o número da sorte!!!***************\n")
        break
    elif(foi_maior):
        print("Escolha um número menor na próxima tentativa")
    elif(foi_menor):
        print("Escolha um número maior na proxima tentativa")
    elif(foi_menor or foi_maior and rodada == 3):
        print("Suas chances acabaram e o jogo também :( ")
    
    
