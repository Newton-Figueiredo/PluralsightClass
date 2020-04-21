'''
funçoes sao estremamente uteis se usaremos ou escreveremos açoes que irao se repetir dentro de um programa
podemos criar blocos de codigos para sesem executados no momento que for mais conveniente
o comando para criar funçoes é o: def
exemplo:
def nome_da_função(variavel1,variavel2)
    bloco de codigo que iremos chamar
    return(o valor para retornar)

obs: nao somos obridagos a fazer uma função com retorno.
'''

#exemplo 1: funçao  que faz o valor quadrado:
def quadrado(x):
    return x*x

print(quadrado(5))

#exemplo 2: função que nao recebe uma variavel de entrada e que nao usam return:
def saudade():
    print("estou com saudades de você bebe!!")

saudade()

# se a função nao tem nenhum argumanto no returno quando chamamos o metodo type() nessa variavel
# ela nos retorna None == True , exemplo:

def quadrado(x):
    print (x*x)

a= quadrado(5)
print(a)
print(type(a))
print(a == None)

print(100*"-")
#podemos chamar funçoes dentro de outras
def quadrado2(x):
    return x*x

def quadruplo(x):
    quad=quadrado2(x) * quadrado2(x)
    return quad

print(quadruplo(5))

#tambem podemos ter varias opçoes de return dentro de uma função 
def escolha(x):
    if x== 1:
        return print("voce escolheu o numero 1")
    elif x==2:
        return print("voce escolheu o numero 2")

print(escolha(1))
print(escolha(2))

#tambem posso retornar mais de uma variavel no return

def getpessoa():
    nome="newton"
    idade="24"
    pais="brasil"
    return nome,idade,pais 

a=getpessoa()
print(a)

#algumas funçoes podem ter nomes especial  e elas  elas usan dunder "__" no inicio e no fim
#exemplo __init__

