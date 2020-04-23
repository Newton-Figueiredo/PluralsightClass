#------- oython type system -------

'''
resumo dessa aula ...

python é caracterizado por ser um sistemas de "tipos" dinamicos
por exemplo, seja essa função:
'''
def soma(a,b):
    return a + b

# vamos chamar essa função de diversas maneiras
# inteiro
print(soma(5,9))
# float
print(soma(5.8,9.7))
# string
print(soma("oi","sumida"))
#listas
print(soma([5,8],[9,3]))
# inteiro + float
print(soma(5,9.1))
# inteiro+ string - vai bugar o programa!!!
#print(soma("oi",9))
'''
podemos ver que python nao faz distinção de tipos a função funciona com todas elas 
a unica meneira de fazer a função "quebrar" seria misturando os tipos 
'''

#---------- scoops---------------
'''
existem 4 tipos de scoops em python alem de uma hierarquia
cada scoop é um contexto em que os nomes sao armazenados e em que podem ser pesquisados
-LOCAL: dentro da função atual
-ECLOSING: funçoes internas
-GLOBAL: no nivel superior do mudulo 
-BUILT-IN: no modulo especial interno
vamos mostrar um exemplo de variavel global e local:
'''
CONTADOR=0
def show_contador():
    print(CONTADOR)

def set_contador(c):
    CONTADOR=c

set_contador(5)
show_contador

#vimos que o valor que retornou foi "0" porque a variavel "CONTADOR" de dentreo da função é local
#para que funcione devemos usar um comando para que a variavel de dentro da função seja a global

def set_contador2(c):
    global CONTADOR
    CONTADOR=c

#chame de novo as funçoes que conseguiremos agora mudar o valor de "CONTADOR"

#---------------- TUDO É UM OBJETO ---------------
'''
podemos verificar sempre o tipo do objeto usando a função "type"
type(nome_do_objeto)
alem de verificar todos os atributos desse objeto usando a função "dir"
dir(nome_do_objeto)
exemplos:
'''
import math
type(math)
dir(math)
