#---------- collections-------
'''
coleçoes comuns em python:
str
bytes
list
dict
for-loops
'''
#----------- STR -------------
#podemos escrever strings com : "" ou ''
frase01="isso é uma string de uma unica linha"
frase02='isso é uma string'

#nao rola fazer strings misturando as duas aspas: " '
#----------- string com multiplas linhas --------------
 frase03="""isso é
 uma string
 de multiplas linhas """

 '''
isso é um comentario de multiplas
linhas.
 '''
#isso é um comentario de uma unica linha
 
 print(frase03)

 #----------------- escape sequence -----------
 frase04="essa é uma frase com tem ums (\") aspa devido colocar essa \ antes da aspa"  
 frase05='essa é uma frase com tem ums (\') aspa devido colocar essa \\ antes da aspa'
# existe uma serie de coisas pra adicionar na frase que usa a barra(backslash) (\)
#va em lexical analise para  de string para ver outras funçoes da (\) em frases

#se tratando de representar variaveis que sao numeros devemos na maioria das vezes 
#convertelas em strings com str(variavel)
a=10
b=str(a)

#tambem podemos percorer strings como listas:

c="cenoura"
print(c[1])

# mesmo chamando c[1] ele nao deixa de ser str:
d=c[1]
type(c)
type(d)

#duvidas ??? use help(str) e veja todas as funçoes aplicaveis as strings
help(str)

#metodos que podemos encontrar no help(str)
c.capitalize()


