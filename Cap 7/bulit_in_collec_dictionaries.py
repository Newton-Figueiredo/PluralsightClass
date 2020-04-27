#------ dicionarios ---------
'''
ja estudamos dicionarios antes, mas aqui vai rolar uma versao mais aprofundada de ferramentas
vamos relembrar aqui 
cada dicionario recebe um par ordenado de informaçoes e eles se chamam de "chave" ou "keys" e "valores" ou "values"
exemplo: dicionario = {key1:value1,key2:value2,key3:value3}
e geralmente consultamos os valores dos valores pela key
'''
dicionario = {'key1':'value1','key2':'value2','key3':'value3'}
print(dicionario)
print(dicionario['key1'])

dicionario = {'key1':'value1','key2':'value2','key3':'value3','key1':'7845'} #esse bloco de codigo ta bugado de propossito
print(dicionario) # os valores da key precisam ser unicos por isso aconteceu esse erro 
print(dicionario['key1'])#dicionarios nao precisam estar em ordem normalmente só guardam dados

#podemos converter pares de tuples em um dicionario vou mostrar um exemplo
nomes_idade=[('newton',27),('pedro',45),('allan',25),('vitao',78)]
agenda=dict(nomes_idade)
print(agenda)

#podemos tambem escrever dicionarios dessa forma:
agenda2=dict(newton=998178381,allan=48452626,pedro=48230563,vitao=45820326)
print(agenda2)

# existe 2 jeitos de copiar um dicionario : exemplo01 é usar o metodo copy:
agenda3=agenda2.copy()
print(agenda3)
# a outra e usar o contrudor dict() e colocar como argumento um dicionario ja existente:
agenda4=dict(agenda2)
print(agenda4)
'''
podemos adicionar o conteudo de um dicionario dentro de outro
usando o metodo update():
'''
material=dict(lapis='445454',caneta='444')
agenda4.update(material)
print(agenda4)
# outro exemplo:
estoque={'borracha':'22','lapis':'33','caneta':'44'}
estoque.update({'borracha':'33','pilha':'66'}) #perceba que o valor de borracha foi atualizado 
print(estoque)

#------------- iteração com dicionarios ---------------------------------
#usando keys como iterador
for key in estoque:
    print(f"{key} : {estoque[key]}")

#usando value como iterador
for value in estoque.values():
    print(value)
#outra forma de fazer:
for key in estoque.keys():
    print(key)
#podemos chamar as keys e values em conjunto 
#para isso usaremos o metodo item() para chamar o par ao inves de um tipo de item
for key,value in estoque.items():
    print(value)
    print(key)

'''
podemos usar testes booleanos como in ou not in
e podemos apagar um item usando del nome-do-dicionario['nome-do-key']

'''
print('newton' in agenda2)
del agenda2['newton']
print(agenda2)
'''
embora as keys dos dicionarios sejam imutaveis e unicas isso nao empede que tenhamos values
flexiveis por exemplo:
 podemos ter uma lista como resposta da value
 '''
letras={'A':[1,2,36],'B':[85,42],'C':[3,6,9]}
print(letras)
letras['A']+=[8,7,9,4]
letras['D']=[9887,11]
