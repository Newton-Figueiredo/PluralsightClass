#--------- compressao --------
'''
sintaxe concisa para descrever listas, conjuntos e dicionários.
'''
#------ compressao de listas ------
'''
maneira rapida e comprimida de criar uma lista 
a partir de uma segunda

muito com para criar listas que dependem de outras sem precisar 
escrever uma função para 'cconverte-las'
exemplo:

[expressao(item) for item in iteravel]

exemplos:
'''
palavras= "mano pablo é um cara legal ele é pro player de lolzinho".split()
print(palavras)

tamanho=[len(palavra) for palavra in palavras]
print(tamanho)

# vou mostrar como isso seria feito sem o conhecimento da compressao de lista

lengths=[]
for word in palavras:
    lengths.append(len(word))

print(lengths) # chegamos ao mesmo resultado da expressao anterior 
# usamos 3 linhas mas com a compressao usamos apenas uma 

# outro exemplo :
from math import factorial
f=[len(str(factorial(x))) for x in range(20)]
print(f)
print(type(f))

#-------------- compressao de conjuntos (set) -------------
'''
coleção de elemantos unicos e desordenados
sets sao mutaveis - podemos adicionar valores ou remover
mas os elementos sao imutaveis - nao podemos editar um slot ou um elemento
'''

s={len(str(factorial(x))) for x in range(20)}
print(s)

#------ compressao de dicionario  ------
'''
cada dicionario recebe um par ordenado de informaçoes e eles se chamam de "chave" ou "keys" e "valores" ou "values"
exemplo: dicionario = {key1:value1,key2:value2,key3:value3}
e geralmente consultamos os valores dos valores pela key

exemplo: {key_expressao(item):value_expressao(item) for item in iteravel}
'''

agenda={"newton":15151621651,"vitu":46848469584,"pablo":54684654,"ander":49684654}

agenda_invertida={numero:pessoas for pessoas,numero in agenda.items()}

print(agenda_invertida)

#----- filtrando compressoes ---- 
'''
existe a possibilidade de colocar condiçoes dentro das compressoes 
no caso de um "if" isso ira filtrar as as infomaçoes que queremos
nas compressoes.
exemplo:
'''
from math import sqrt
def numero_primo(x):
    if x < 2:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            return False
    return True

numeroprimo=[x for x in range(101) if numero_primo(x)]
print(numeroprimo)
