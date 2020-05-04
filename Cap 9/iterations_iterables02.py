#---- protocolo de iteração ------
'''
precisamos definir e diferenciar o que é um iteravel e um iterador
iteravel:
tem os elementos que o iterador ira usar para os laçoes de repetição
podemos trabalhar com o iteravel usando o metodo iter()

iterador:
é o elemento que usaremos para manipular nos laços 
podemos usar o metodo next() para percorer o iterador

exemplo: iterador = iter(iteravel)
next(iterador)

podemos parar iteraçoes com o uso das exeçoes (except)

quando chamarmos next() e a lista do iterador 
acabar de percorrer todos os argumentos vai acontecer um erro
stopiteration

exemplo:

'''
clima=['verao','inverno','outono','primavera']
iterador=iter(clima)
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador)) # nesta tentativa de chamar o quinto argumento vai bugar o programa

# vamos ao proximo exemplo de evitar a execao de stopiteration

def proximo():
    clima=['verao','inverno','outono','primavera']
    iterator=iter(clima)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("o iterador está vazio")

