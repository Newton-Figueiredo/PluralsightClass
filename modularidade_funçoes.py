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
