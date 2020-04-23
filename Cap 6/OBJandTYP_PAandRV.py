#-----overview-----------
'''
-------------Objetos e Tipos-----------------
em resumo tudo é um objeto .....
quando criamos uma variavel, python cria um objeto com aquele valor e o atribui um id
por exemplo:
x = 1000
se usarmos: 
id(x)
veremos em que id x está atribuido 

de falarmos agora que;
y = 1000 
e usarmos:
id(y)
percebemos que ambos possuem a mesma id....
pq o objeto inteiro "1000" é o mesmo para as duas variaveis ...

se o argumento de dentro da variavel for 1000/2 o id sera difetente de uma variavel que tem 500

exemplo:
'''
x=1000
y=1000

print(id(x))
print(id(y))

t=500
j=500
r=1000/2

print(id(t))
print(id(j))
print(id(r))
print(j is r)

'''
a mesma coisa acontece com listas:

'''

a=[1,2,3]
b=a
print(id(a))
print(id(b))

#quando mudamos um valor em a tambem muda em b, pelo fato deles dividirem o mesmo objeto
a[0]=17
print(a)
print(b)
print(id(a))
print(id(b))

#vamos tertar outra teoria
a=[1,2,3]
c=[1,2,3]
# a e c possuem os mesmos valores ...
print(id(a))
print(id(c))
print(a == c)
print(a is c)

'''
concluimos que:
mesmo a e c tendo os mesmos valores eles nao sao os mesmos objetos
vemos que as duas tem ids diferentes
e o metodo is da FALSE justamente devido a isso 
mas o metodo == confirma que as duas possuem is mesmos valores

'''
#---------Passando argumentos e Retornando Valores -----------------
'''
esse capitulo fala da possibilidade de uma lista enrar numa função e ser
modificada ou copiada.
mas o que concluimos foi que a função nao copia a lista mas sim tem como referencia
o mesmo objeto na qual a lista que foi inserida na funçao.
exemplo:
'''
c=[1,2,3]

def f(a):
    return a

g=f(c)

print(c is g)

