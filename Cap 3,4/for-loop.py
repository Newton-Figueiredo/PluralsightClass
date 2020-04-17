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


#------------------ Botando Tudo Junto !!!!! ---------------------
from urllib.request import urlopen
story=urlopen("http://sixty-north.com/c/t.txt")
story_words=[]

for line in story:
    line_words=line.decode("utf8").split()
    for word in line_words:
        story_words.append(word)

story.close()
