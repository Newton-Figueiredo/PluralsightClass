#--------------- Dicionarios ----------------------
'''
- estutura de dados fundamental em python
-atribuição de valores as "chaves"
exemplo:
contatos={"danielle":"998455653","larissa":"987856365","joyce":"985842210"}
as pessoas sao as "chaves"
e os numeros os "valores"

para cada chave existe um valor atribuido e podemos acessar apenas chaves ou apenas valores 
como tambem os dois ao mesmo tempo.
'''
contatos={"danielle":"998455653","larissa":"987856365","joyce":"985842210"}

print(contatos["danielle"])
print(contatos)

contatos["newton"]="998178381"
print(contatos)

#podemos criar um dict vazio...
e={}
print(type(e))
