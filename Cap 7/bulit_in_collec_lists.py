#---------- listas -------
'''
ja vimos listas antes nesse curso mas o cara vai passar das dicas supremas
'''
#----- indeces negativos -----
'''
em resumo o indice negativo faz o usuario percorrer a lista de tras pra frente 
de a lista 10 slots e o ultimo slot seria [9] poderiamos ter usado[-1] chegariamos ao mesmo resultado
exemplo:
'''
lista=[9,8,7,6,54,9,1]
print(lista[-1])

#------------ slicing---------
'''
consiste em consultar uma lista podemos acessar qualquer pedaço desde que deteminemos esse intervalo
exemplo: nome_da_lista[inicio:fim]
'''
print(lista[0:2])
print(lista[2:4])
print(lista[2:])
print(lista[:3])
print(lista[:])

#com slice podemos copiar uma lista (de fato)
#nesse metodo mesmo a lista2 nao tendo o mesmo id da lista um os valores internos sao os mesmos objetos
lista2=lista[:]
print(lista2)
print(lista2 is lista)
print(lista2 == lista)
#mais uma forma de copiar:
lista3=lista.copy()
print(lista3)
print(lista3 is lista)
print(lista3 == lista)
#mais uma forma de copiar:
lista4=list(lista)
print(lista4)
print(lista4 is lista)
print(lista4 == lista)

#CUIDADO QUANDO FOR COPIAR COM [:] e tambem com copy() -----------------------------------------------------------------------------
A=[[1,2],[5,6]]
B=A[:]
A[0]=[8,8,8]
print(A)
print(B)
A[1].append(7) #quando fizemos esse operação a lista b recebeu o mesmo append mesmo sendo uma lista diferente
print(A)
print(B)  #mas o objeto dentro da lista mais externa é igual para os dois !
#--------------------------------------------------------------------------------------------------

#--------------------------------outra coisa importante --------
lista5=[[1,2]]
lista5=lista5*4
print(lista5)
lista5[2].append(7) #quando adicionamos qualquer valor num slot todos recebem o mesmo append
print(lista5) #devido a todos os itens internos serem derivados do mesmo objeto
#----------------------------------------------------------------------
'''
quando precisamos procurar a posição dentro de uma lista usamos o metodo index()
exemplo: nome_da_lista.index("objeto_buscado")

podemos tambem contar quantas vezes a mesma palavra ou objeto tem em uma lista, usamos count()
exemplo: nome_da_lista.cont("objeto_buscado")

podemos remover um objeto da lista usando del[]
exemplo: del nome_da_lista["posiçao_objeto_buscado"[]

podemos remover pelo nome do objeto usando remove()
exemplo: nome_da_lista.remove("objeto_buscado")

podemos colocar objetos na lista de uma maneira diretende do append, ao usarmos insert dizemos
a posição e o que vamos por
exemplo:nome_da_lista.insert(posição_index,oque_vamos_por)

podemos concatenar listas com o sinal de + mas para fazer isso de modo mais eficiente existe o metodo
extend()
exemplo:nome_da_lista.extend([oque_vamos_por1, oque_vamos_por2, oque_vamos_por3])
'''
print(lista.count(9))
print(lista.index(9))
print(lista)
lista.remove(9) #essa list tem dois 9 mas ele so apagou um e no caso o de index mais proximo
print(lista)
del lista[0]
print(lista)
lista.insert(0,789)
print(lista)
lista.extend([1,2,3,4])
print(lista)

'''
existem metodos que ajudam a organizar suas listas 
usaremos 
reverse()
sort() - organiza por tamanho ou crescente ou decrescente (os que ja vi)
sort() - crescente
sort(reverse=True) - decresente
sort(key=len) - por tamanho de quantidade de caracteres (comum em strings)

'''
print(lista)
lista.sort() #tambem podemos usar sorted(nome_da_lista)
print(lista)
lista.reverse() #tambem podemos usar reverced(nome_da_lista) 
print(lista)