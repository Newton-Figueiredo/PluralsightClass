#------strings----
'''
ja vimos strings em outras aulas, mas aqui vamos aprofundar um pouco nossos conhecimentos 

'''
#tamanho da string:
a=len("e ai galerinhaaaaaaaaaaaaa")
print(a)
#concatenando strings:
b="hoje "+"vai "+"rolar "+"putaria!"
print(b)
c="newtinho "
c+="é um cara "
c+="legal"
print(c)
'''
strings são imutaveis nao podemos modificalas pontualmente (como nas listas)
mesmo que exista a o simbolo + para concatenar existe um metodo para adicionar palavas as strings 
join()
devemos das prioridade para ele ou invez de usar o +
'''
cores= ";".join(["azul","vermelho","amarelo","rosa"])
print(cores)
print(cores.split(";"))
palavra="".join(["new","ton"])
print(palavra)
# em resumo join precebe o separador e uma lista de strings : "separador".join([lista_de_strings])

'''
vamos aprender agora outro metodo partition
ele separa uma string em 3 partes
"frase_que_vamos_separar".partition("pedaço_que_vamos_partir")
exemplo:
'''
q="pabloégay".partition("é")
print(q)
print(type(q))
#podemos capturar palavras e por em variaveis com o partition:
a,b,c = "brasil:brasilia".partition(":")
print(a)
print(b)
print(c)

af,_,cf = "brasil-brasilia".partition("-")
print(af)
print(_)
print(cf)

'''
vamos aprender outro metodo "format"
format subistitue valores marcados por "{numero}" na sequancia de argumentos recebidas pelo metodo:
exemplo:
'''
texto="a idade de {0} é de {1}, mas {0} faz aniversario no dia {2} e de mes {3}".format("newton","24","27","outubro")
print(texto)
#tambem da pra escrever dessa forma: ele vai seguir a sequencia dentro dos parenteses
texto2="pablo é {} {}".format("muito","gay")
print(texto2)
#outra maneira:
texto3="pablo é {intensidade} {sexualidade}".format(intensidade="muito",sexualidade="gay")
print(texto3)

'''
existe varias maneiras de fazer uso de format mas para casos nao tao repetitivos
ele nao se aplica muito bem .
para isso nos temos as f-strings!
'''
#----------------------- f-Strings--------------------------
'''
expreçoes de sintaxe minimas imbutidas em strings
exemplos:

'''
print(f"quando sera a soma de 1+1 = {1+1}")
valor=4*20
print(f"o valor é:{valor}")
#podemos importar funçoes tambem
import math
print(f"as contante matematicas são:pi={math.pi:.3f}, e={math.e:.3f}: ")
'''
podemos sempre consultar todos os metodos das strings com o comando help(str)
'''
