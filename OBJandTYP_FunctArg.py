#------ default argument value ------
def banner(mensagem,borda="-"):
    linha=borda*len(mensagem)
    print(linha)
    print(mensagem)
    print(linha)

'''
observe essa função: normalmente funçoes esperam valores dos usuarios
no caso a variavel borda já possui um valor pré-estabelecido 
existe duas maneiras de chamar essa função....

texto="pablo é gay"

primeira:
    banner(texto)
segunda:
    banner(texto,"*")

vamos chamar na pratica!
'''
texto="pablo é muito gay"
banner(texto)
banner(texto,"*")
banner(texto,"¬")

#dica: o valor default é bom para variaveis fixas
#se usar variaveis dinamicas existe a chance de dar uma merda grande! em resumo.
# outro exemplo de função com valor default que trola o usuario :

def add_spam(menu=[]):
    menu.append("spam")
    return menu
cafe=['ovo','pao']
almoco=['arroz','batata']
add_spam(cafe)
add_spam(almoco)
add_spam()
add_spam()
add_spam(cafe)
print(cafe)
print(almoco)
print(add_spam())
'''
add_spam tinha um vetor vazio declarado dentro dele, toda vez que ele era chamado..
ele salva-va "spam" dentro desse vetor "menu" que já nao estava mais vazio...
nao cumprindo assim com o seu objetivo de nao armazenar mais de um valor spam 
'''