#------OVERVIEW---------
#inteiro
10
#chamando um numero binario (0b)
0b10
#chamando um numero hexadecimal (0x)
0x10
#covertendo variavel em inteiro (int()):
int(3.5)
#covertendo variavel em decimal (float()):
float(3)
#escrevendo em notação cientifica (e):
3e8
1.61e-5
#operador none:
a = None
a == None
a
 #operadores logicos: True e False
 bool(0)  #apenas zero é considerado falso
 bool(10)
 bool(-10)
 bool(0.0)
 bool(0.225)
 bool("") #apenas strings vazias é considerado falso
 bool([]) #apenas listas vazias é considerado falso
 bool([1,2,3])
 bool("False") 
 
 #--------RELATIONAL OPERATOR --------
 """ 
 == igualdade:
 != diferente:
 < menor que:
 > maior que:
 <= menor e igual a que:
 >= maior e igual a que:
 """
g=20    # atribuindo
g == 20 # verdade
g ==13  # falso
g != 13 # verdade
g < 30  # verdade
g <= 20 # verdade
g > 30  # falso

#-------------- CONTROL FLOW ---------------
# if expressao: 
#     bloco com comando

if True:
    print("é verdadeiro!")

if bool("ovos"):
    print("sim, por favor !")

h=42
if h > 50:
    print("Maior que 50")
else:
    print("50 ou menor") 

if h > 50:
    print("Maior que 50")
else:
    if h < 20:
    print("Menor que 20")
    else:
    print("entre 20 e 50") 

if h > 50:
    print("Maior que 50")
elif h < 20:
    print("Menor que 20"))
else:
    print("entre 20 e 50")

# --------------------- WHILE-LOOPS ---------------
# while expressao:
#      bloco de codigo
#obs : a expressao que fica no while se torna numa condição booleana e enquanto verdadeira roda o codigo

c=5
while c != 0:
    print(c)
    c -= 1

# outra forma de fazer o loop devido a expressao ser booleana
c=5
while c :
    print(c)
    c -= 1
# chegaremos no mesmo resultado porque a variavel só se torna falsa quando ela chega a "zero"
while True:
    r=input()
    if int(r)%7==0:
        break

