#------docstrings-------
#-*- coding: utf-8 -*-
'''
docstrings são testos que preparamos para serem acessados pela função help do python
elas precisam ser escritas dentros das funçoes  "def" para serem lidas pelo "help"
exmplo: 

o arquivo tambem pode ter uma docstring quando usamos a help vemos todas as docstrings de todas as 
funçoes

'''
"""
este arquivo contem um copilado de funçoes matematicas:
"""
def quadrado(x):
    """
    a função quadrado retorna o numero escolhido ao quadrado,
    adiicione um numero (int), que a função retornara um numero(int).
    
    """
    q=x*x
    return q


'''
vai ficar com esse aspecto:

Help on function quadrado in module modularidade_docstring:

quadrado(x)
    a função quadrado retorna o numero escolhido ao quadrado,
    adiicione um numero (int), que a função retornara um numero(int).
(END)
'''