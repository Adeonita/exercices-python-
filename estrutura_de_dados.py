lista =	[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]


#Função retorna par
def numeros_pares(lista):
    numeros= []
    for number in lista:
        if(number % 2 == 0):
           numeros.append(number)
    
    print(numeros)
    

#Função retorna média
def media(lista):
    soma = 0
    tamanho_da_lista = len(lista)
    for elementos in lista:
       soma = (soma + elementos)
       media = soma /tamanho_da_lista
    return(media)

#Função soma negativos
def soma_negativos(lista):
    soma = 0
    for elementos in lista:
        if(elementos < 0):
            soma = soma - elementos
    return(soma)    

maior_elemento = max(lista)
menor_elemento = min(lista)
ocorrencias_do_primeiro = lista.count(lista[0])
media = media(lista)
soma_negativos = soma_negativos(lista)


print("O maior elemento é: {}".format(maior_elemento))
print("O menor elemento é: {}".format(menor_elemento))
print("A quantidade de ocorrências do elemento {} é : {}".format(lista[0], ocorrencias_do_primeiro))
print("A média entre os numeros da lista é: {}".format(media))
print("Os numeros pares são:  ") 
numeros_pares(lista)
print("A soma dos numeros negativos é: {}".format(soma_negativos))