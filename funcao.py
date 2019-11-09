def velocidade(espaco, tempo):
    velocidade = (espaco/tempo)
    return(velocidade)

espaco = int(input("Insira o espaco percorrido: "))
tempo = int(input("Insira o tempo gasto: "))

velocidade = velocidade(espaco, tempo)
print("A velocidade foi de {} m/s".format(velocidade))