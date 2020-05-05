#------- geradores---------------
'''
Os geradores em Python são uma maneira simples de criar 
um objeto iterável sem a necessidade de construí-lo dentro de 
uma classe

Em todos os aspectos uma função geradora é uma função 
como qualquer outra. Sua principal diferença está no fato de 
não utilizar a instrução return, que encerra a execução e envia
o resultado, e sim a instrução yeld, que passa um elemento/resultado
parcial mas não interrompe a execução desta.

Claro que não existe uma regra ou norma que diga exatamente onde 
um gerador deve ser utilizado ou onde é melhor trabalhar com 
funções convencionais, isto dependerá exclusivamente do programador 
mas o uso de geradores permite economizar memória ao dispensar a 
criação de variáveis para armazenamento temporário do que está 
sendo processado pelo programa.

exemplo de funçoes geradoras:
'''
'''
def sequencia():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a,b = b,a+b

for x in sequencia():
    print(x)
'''

#-------------- espressoes geradoras --------------------
'''
podemos escrever geradores de manaira mais simples e direta
esse tipo de sintaxy lembra as compressoes de listas
exemplo01:

funçao_geradora=(expressao(iterador) for iterador in iteravel)

podemos tambem usar uma função + a espressao do gerador : exemplo02:
função((expressao(iterador) for iterador in iteravel))
'''
quadrado=(x*x for x in range(1,10))
print(list(quadrado))
print(list(quadrado)) # perceba que quando chamamos pela segunda vez a lista retorna vazia 
# funçoes geradoras só armazena e executa uma unica vez eles nao guardam na memoria (para nao gastar espaço)

# para recriar um gerador, devemos chamar a espressao geradora de novo

print(sum((x*x for x in range(1,10))))

#------------------ intertools---------------
'''
existe uma biblioteca inteira para se trabalhar com iteradores e
de tabela com geradores podemos importalas da biblioteca intertools
exemplo:
from intertools import nome_do_metodo

vou listar alguns aqui como exemplo mas devemos ver na internet 
as outras opçoes
enumerate()
sum()
https://docs.python.org/pt-br/3/library/itertools.html
'''