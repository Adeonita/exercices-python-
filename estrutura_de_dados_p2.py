lista = []

def insere_dados(lista):
    nome = input("Digite seu nome: ")
    lista.append(nome)
    sobrenome = input("Digite seu sobrenome: ")
    lista.append(sobrenome)
    idade = input("Digite sua idade: ")
    lista.append(idade)
    return(lista)

print(insere_dados(lista))

    

