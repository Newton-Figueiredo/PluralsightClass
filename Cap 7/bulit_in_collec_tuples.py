#------- tuples ----------
'''
lista imutavel de objetos arbitrarios
os objetos dentro delas nao podem ser substituidos ou removidos 
tuples tem sintaxe parecida com a das listas
exemplo:
'''
t=("oi sumida",254,5.58)
print(t[0])
print(t[1])
print(t[2])
print(len(t))
#podemos usa-lo no "for"
for itens in t :
    print(itens)
# podemos concatenar o tuple
b=t + ("e ai gente ....", 122222222)
print(b)
print(b*3)
# podemos colocar tuples dentro de outras, e ter acessos a seus elementos
c=((1,2),(2,5),(5,9))
print(c[1][0])
#para criar uma tupla de um unico elemento é obrigado a por um virgula ","
d=(25555,)
# se nao por... quando chamarmos type() vai dar um tipo diferente de tuple....
# podemos criar uma tuple vazia:
e=()
# e podemos crialas sem os parenteses:
p= 1, 2, 1, 23, 5
print(type(p))
#podemos usar alguns metodos :
print(min(c))
print(max(c))

#-------------------- descompactação de tuple-----------------------
#podemos atribuir os valores de dentro da tuple para variaveis fazendo que elas deixem a tupla
#todos os exemplos que vi, atribuiam todos os elementos exemplo:
(v,(f,g))=(8,(4,5))

#podemos tambem trocar variaveis de lugar 
nome1="newton"
nome2="aline"
nome1,nome2 = nome2,nome1
print(nome1)
print(nome2)

#podemos criar tuples das sequintes maneira:
#colocando uma lista dentro:
tuple([1,2,3,4])
#colocando uma frase(string):
tuple("oi sumida")
#obs tambem da certo pondo a variavel dentro do metodo.
frase="oi sumida"
frase=tuple(frase)
