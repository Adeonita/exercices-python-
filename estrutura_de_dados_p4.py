
def insere_pessoa():
    insere_pessoa = True
    lista = []
    while(insere_pessoa):
        print("\nCadastro de pessoa, insira os dados solicitados\n")
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        cidade = input("Digite a cidade: ")
        pessoa = dict(nome  = nome, idade = idade, cidade = cidade )
        lista.append(pessoa)
        resposta = input("\nDigite 1 para cadastrar nova pessoa e 0 para listar: ")
        if(resposta == '0'):
            insere_pessoa = False

    return(lista)

lista = insere_pessoa()

def exibe_pesoa(lista):
    for pessoa in lista:
        #Para pegar um atributo de um dict se usa a função get
        print("\nNome: {}".format(pessoa.get('nome')))
        print("Idade: {}".format(pessoa.get('idade')))
        print("Cidade: {}".format(pessoa.get('cidade')))
        

print("\n**********Pessoas cadastradas no sistema**********\n")
exibe_pesoa(lista)
