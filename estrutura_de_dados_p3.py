media = 0

def calcula_media():
    nota1 = int(input("Insira a 1ª nota: "))
    nota2 = int(input("Insira a 2ª nota: "))
    nota3 = int(input("Insira a 3ª nota: "))
    nota4 = int(input("Insira a 4ª nota: "))

    media = (nota1 + nota2 + nota3 + nota4) / 4

    return(media)


print("A media foi: ",calcula_media())