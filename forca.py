print("\nBem vindo ao jogo da Forca\nVocê deverá advinhar qual a palavra secreta")

palavra_secreta = "banana"
letras_acertadas = ['_','_','_','_','_','_']
eh_uma = "Fruta"
tamanho_palavra = len(palavra_secreta)
acertou = False
enforcou =  False
acertos = 0
erros = 0
pontos = tamanho_palavra*2
ganha_ponto = 5
perde_ponto = pontos/tamanho_palavra

print("\nA palavra tem {} letras e é um(a) {}\nA cada erro você perde {} pontos\nO Jogo começou, e você tem {} pontos".format(tamanho_palavra, eh_uma,perde_ponto, pontos))
print("\n {}".format(letras_acertadas))

while(not acertou and not enforcou):
    print("\nJogando...")
    chute = input("\nEscolha uma letra: ")
    
    
    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
                acertos = acertos + len(letra)
                if(acertos == tamanho_palavra):
                    acertou = True   
            index = index + 1
    else:
        erros = erros + 1
        pontos = pontos - perde_ponto
        print("Você agora tem {} pontos".format(pontos))
        if(erros == tamanho_palavra + 3 or pontos == 0):
           enforcou = True 
    print("\n {}".format(letras_acertadas))
    
    
    if(acertou):
        print("Parabens, você venceu o jogo")
    if(enforcou):
        print("Suas chances acabaram, e o jogo também :(")
