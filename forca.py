print("\nBem vindo ao jogo da Forca\nVocê deverá advinhar qual a palavra secreta")

palavra_secreta = "banana"
letras_acertadas = ['_','_','_','_','_','_']
eh_uma = "Fruta"
tamanho_palavra = len(palavra_secreta)
acertou = False
enforcou =  False
acertos = 0

print("\nA palavra tem {} letras e é um(a) {}".format(tamanho_palavra, eh_uma))

while(not acertou and not enforcou):
    print("\nJogando...")
    chute = input("\nEscolha uma letra: ")
    
    index = 0
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
            acertos = acertos + len(letra)
            if(acertos == tamanho_palavra):
                acertou = True   
        index = index + 1
    
    print(letras_acertadas)
    
    if(acertou):
        print("Parabens, você venceu o jogo")
