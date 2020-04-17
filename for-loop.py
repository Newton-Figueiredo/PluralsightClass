'''
esse loop é maravilhoso ele precisa de um item e um iteravel para funcionar
exemplo:
 
for "item" in "iteravel":  
    print(item)

#essas ("") nao sao usadas no laço é so pra diferenciar o comando da variavel. 
vamos ver na pratica varios exemplos:
'''
a=["laranja","maça","abacaxi"]
b=[1,3,7]
contatos={"danielle":"998455653","larissa":"987856365","joyce":"985842210"}

for iten in a:
    print(iten)   


for itens in b:
    print(itens*3)

for pessoas in contatos:
    print(pessoas,contatos[pessoas])
    