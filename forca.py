print("\nBem vindo ao jogo da Forca\nVocê deverá advinhar qual a palavra secreta")

palavra_secreta = "banana"
letras_acertadas = ['_','_','_','_','_','_']
eh_uma = "Fruta"
tamanho_palavra = len(palavra_secreta)
acertou = False
enforcou =  False
acertos = 0
erros = 0
pontos = 10
perde_ponto = pontos/tamanho_palavra

print("\nA palavra tem {} letras e é um(a) {}".format(tamanho_palavra, eh_uma))
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
        if(erros == tamanho_palavra):
           enforcou = True 
    print(letras_acertadas)
    
    
    if(acertou):
        print("Parabens, você venceu o jogo")
    if(enforcou):
        print("Suas chances acabaram, e o jogo também :(")
