#--------------- sets -----------------
'''
coleção de elemantos unicos e desordenados
sets sao mutaveis - podemos adicionar valores ou remover
mas os elementos sao imutaveis - nao podemos editar um slot ou um elemento
exemplos:
'''

p={1,2,3,4,5,6} #sets parecem dicionarios mas nao possuem par 
print(p)
print(type(p))
d={} # e comum errrmos ao criar sets vazios, já que se parecem com dicionarios 
print(type(d))
e=set() #maneira correta de criar um set vazio
print(type(e))
#tambem podemos criar sets dessa maneira:
a=set([2,3,5,6,89,74])
#podemos converter listas em sets desde que elas nao tenham elementos repetidos
lista=[1,2,3,1,4,3]
b=set(lista)
print(b) #quando convertemos a lista em set ela apagou todos os valores repetidos
'''
podemos usar sets em operadoes logicos tais como:
in
not in
e podemos usar sets em loops
'''
for valores in b:
    print(valores)

print('52' in b)
print('52' not in b)
# adicionando um elemanto simples ...usamos o metodo add()
b.add(52)
print(b)
#adicionando varios elementos de uma vez devemos usar o metodo update()
b.update([89,65,45])
print(b)
# removendo itens dos sets usamos o metodo remove() caso o elemento nao exista no set ele vai dar erro
b.remove(52)
print(b)
'''existe um metodo de apaguar elementos dos sets e mesmo que ele eleemento nao exista o programa nao vai
gerar erro o nome do metodo é discard()'''
b.discard(52)
print(b)
#podemos copiar sets .... com o metodo copy()
h=b.copy()
print(h)
#da mesma forma que da pra copiar por:
m=set(b) 
print(m)
'''
a parte mais importante de sets vai rolar agora 
sets possuem testadores de conjuntos a galera de ALGEBRA se amarra é uma parada sobre 
CONJUNTOS E SUB-CONJUNTOS
-UNIOES (une dois conjuntos sem repetir valores em comum aos dois ) conjunto1.union(conjunto2)
-DIREFENÇAS (mostra apenas os valores que nao se repetem entre o conjunto1 no conjuntos) conjunto1.difference(conjunto2)
-INTERSEÇÃO (mostras apenas os elementos iguais dos dois conjuntos) conjunto1.intersection(conjunto2)
-SUBCONJUNTOS (verifica se um conjunto esta dentro do outro )conjunto1.issubset(conjunto2)
-SUPERCONJUNTOS (verifica se todos os elementos do segundo conjunto estao presentes no primeiro )conjunto1.issuperset(conjunto2)
-CONJUNTO SEPARADO (verifica se dois conjuntos nao tem menbros em comum) conjunto1.isdisjoint(conjunto2)

conjunto1.symmetric_difference(conjunto2) (parecido com a DIFERENÇAS
 mas agora mostra a diferença unilateral dos dois conjuntos)


'''
