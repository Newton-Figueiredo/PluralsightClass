'''
-------LEMBRETE: refatorar esse programa adicionando os metodos: list() e range(inicio,parada,passo): ------------
'''

from random import choice 

Dados=[]
Lados=[]
gamelocal=True
gameglobal=True

print("Fala galera partiu jogar esse RPG... só escolherem seus Dados e partiiiu!!")

while gameglobal==True:

    ndados=int(input("De quantos dados voce precisa?: "))
    nlados=int(input("Os dado que voce precisa é de quantos lados ?: "))
    
    for lados in range(nlados):
        Lados.append(lados+1)


    while gamelocal==True:
            nndados=ndados

            if ndados >=2 and nlados >0 :
                print("Lançando os Dados!!!!")
                for dados in range(nndados):
                    Dados.append(Lados)
                    print(f"Valor do Dado Nº:{dados+1} é: {choice(Dados[dados])}")
            elif ndados == 1 and nlados >0 :
                print("Lançando o Dados!!!!")
                print(f"Valor do Dado é: {choice(Lados)}")
            elif ndados <=0 or nlados <=0 :
                print("Não vale trollar o programinha :3 ")
            
            resposta=str(input("Vamos continuar nesse modo ?:((s) para sim ou (n) para nao):"))
            if resposta == "s":
                gamelocal=True
            elif resposta == "n":
                gamelocal=False
        
    resposta=str(input("Vamos continuar com o gerador de dado ?:((s) para sim ou (n) para nao):"))
    if resposta == "s":
        gameglobal=True
        gamelocal=True
    elif resposta == "n" :
        gameglobal=False
        print("Até a proxima!!!!")    
    
        
