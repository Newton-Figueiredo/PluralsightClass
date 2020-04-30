#----------exception handling--- tratamento de exceçoes-----
'''
mecanismo para interromper o fluxo normal do programa e continuar no contexto do "erro/problema"
circundante.

'''
#------------ execeçoes e controle de fluxo ---------------
'''
o codigo a seguir converte strings em inteiros , vamos executa-lo e gerar um erro de "entrada"
proposital, vejamos o que acontece.

para isso devemos importar no repl e chamarmos a função convert("frase_de_exemplo".split())
'''
DIGIT_MAP = {
    'zero':  '0',
    'one':   '1',
    'two':   '2',
    'three': '3',
    'four':  '4',
    'five':  '5',
    'six':   '6',
    'seven': '7',
    'eight': '8',
    'nine':  '9',
}


def convert(s):
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x

'''
vamos analisar o erro que apareceu:
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/newton/pluralsight/getting-started-python-core/getting-started-resources/m08/clip-02/use-convert-v1/exceptional.py", line 18, in convert
    number += DIGIT_MAP[token]
KeyError: 'tree'

oque aconteceu é que o quando colocamos um valor que nao pode ser convertido "tree" o DIGIT_MAP 
nos retorna dizendo que o valor tree nao está dentro das possibilidades a serem retornadas
portanto a exceçao foi capiturada pelo repl e exibido o erro de chave... ja que DIGIT_MAP 
é um dicionario e dicionarios possuem keys e values.....
que no caso ele claramente diz que nao conseguiu achar a key:"tree"....
'''

#--------- handling exceptions ---- tratamento de excecoes ----------
'''
tratamento de excecao é justamento pegar o erro e retornar
algo que voce queira, temos varias maneiras de tratar esses erros e vamos mostrar aqui
alguns casos.
é o caso do metodo try: - except: ele lembra o if: - else: ou o do:- while: mas da versao de python
exemplo:
'''

def convert(s):
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except KeyError: #---- caso a tentativa gere um erro... faça: -----
        x= -1 #--- como lidar com a excecao
        print("conversao falhou")
        return x

'''
perceba que o nosso except esta lidando com keyErrors entao se por acaso eu colocase uma variavel
do tipo int o programa geraria um erro de tipo e mostraria o erro .....

para evitarmos isso tambem devemos dizer para a nossa função caso ele cometa um erro de tipo...
(o programa espera strings caso ele coloque numeros vai dar esse erro)
'''

def convert(s):
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except KeyError: #---- caso a tentativa gere um erro... faça: -----
        x= -1 #--- como lidar com a excecao
        print("conversao falhou")
        return x
    except TypeError: #---- caso a tentativa gere um erro... faça: -----
            x= -1 #--- como lidar com a excecao
            print("conversao falhou")
            return x

'''
agora estamos evitando da nossa função de retornar dois tipos de eventuais erros e dando uma continu-
idade ao programa sem que o REPL nos interrompa com as excecoes.

mas perceba que estamos duplicando o nosso codigo ... estamos pedindo para que ele retorne a mesma coisa 
com dois tipos de erros direfentes ... podemos tentar sinplificar essa função

refatorando :
'''
def convert(s):
    x= -1 
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except (KeyError,TypeError): #---- caso a tentativa gere um erro... faça: -----
        print("conversao falhou") #--- como lidar com a excecao
        return x

'''
pronto conseguimos colocar dois erros na mesma except... assim conseguimos simplificar nosso
codigo e tornar ele mais eficiente.
'''
#-------------- execeoes causadas por erro de programadores ------------
'''
erro de identação
erro de sintaxe
erro de nome
esses sao os erros mais comuns, que sao causados pelo programador 

vamos dar um exemplo

'''

def convert(s):
    x= -1 
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except (KeyError,TypeError): #---- caso a tentativa gere um erro... faça: -----
        #print("conversao falhou") #--- como lidar com a excecao
        return x

'''
retiramos o print "conversao falhou" ja que temos a except funcionando ...
nao queremos mais printar o aviso ...

ao chamarmos essa função ela vai gerar erro de identação ...

quando chamamos except ele espera algum argumento ...
quando tiramos o print ele ficou esperando algum bloco de codigo e acabou acusando
o erro...

uma maneira de fazer esse programa funcionar é colocar o argumento pass
exemplo:
com o pass o programa vai ignorar o resto do bloco e continuar o programa
'''

def convert(s):
    x= -1 
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except (KeyError,TypeError): #---- caso a tentativa gere um erro... faça: -----
        #print("conversao falhou") #--- como lidar com a excecao
        pass #--- isso vai corrigir o programa --- 
        return x

#------------ acessando os objetos da execçao -------------
import sys
def convert(s):
    x= -1 
    try: #--- tente -> isso.. -----
        number = ''     #----bloco que pode gerar uma excecao.... -----
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao deu certo")
        return x
    except (KeyError,TypeError) as e: #---- guardando os argumantos dos erros na variavel "e"
        print(f"o erro foi de: {e!r}",file=sys.stderr)  #vamos printar o erro o objeto do erro esta salvo na variavel "e"
        return x                      # "file" recebe o nome que o usuario digitou, que o casionou o erro.
                                      # o comando !r  adociona(une) a variavel "e" na string do print