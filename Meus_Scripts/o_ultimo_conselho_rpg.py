from random import choice

def ler_texto(nome_do_arquivo,linha_inicio,linha_fim):
    f=open(nome_do_arquivo,mode='rt',encoding='utf-8')
    lines=f.readlines()
    contador=1
    for line in lines:
        if contador<=linha_fim and contador>=linha_inicio:
            print(line)
        contador+=1
    f.close()

def batalha(sua_arma):
    arma_inimigo=jokenpo()
    if sua_arma==arma_inimigo:
        condicao=1
        return condicao
    else:
        if sua_arma=="Pedra" and arma_inimigo=="Tesoura":
            condicao=2
            return condicao
        elif sua_arma=="Papel" and arma_inimigo=="Pedra":
            condicao=2
            return condicao
        elif sua_arma=="Tesoura" and arma_inimigo=="Papel":
            condicao=2
            return condicao
        elif arma_inimigo=="Papel" and sua_arma=="Pedra":
            condicao=3
            return condicao
        elif arma_inimigo=="Pedra" and sua_arma=="Tesoura":
            condicao=3
            return condicao
        elif arma_inimigo=="Tesoura" and sua_arma=="Papel":
            condicao=3
            return condicao
            
        
        

def jokenpo():
    lados=["Pedra","Papel","Tesoura"]
    escolha=choice(lados)
    return escolha

def main():
    

    print("""
    
      ____    _    _  _  _    _                      _____                          _  _                      
     / __ \  | |  | || || |  (_)                    / ____|                        | || |                     
    | |  | | | |  | || || |_  _  _ __ ___    ___   | |      ___   _ __   ___   ___ | || |__    ___            
    | |  | | | |  | || || __|| || '_ ` _ \  / _ \  | |     / _ \ | '_ \ / __| / _ \| || '_ \  / _ \           
    | |__| | | |__| || || |_ | || | | | | || (_) | | |____| (_) || | | |\__ \|  __/| || | | || (_) |  _  _  _ 
     \____/   \____/ |_| \__||_||_| |_| |_| \___/   \_____|\___/ |_| |_||___/ \___||_||_| |_| \___/  (_)(_)(_)
    """)
    
    start=str(input("Aperte 's' para começar."))
    
    while start in ["s","S"]:
        ler_texto("intro.txt",1,15)
        resposta=int(input())
        if resposta == 1:
            ler_texto("intro.txt",16,24)
            resposta=int(input())
            if resposta == 1 :
                ler_texto("intro.txt",31,45)
                resposta=int(input())
                if resposta == 1 :
                    condicao=1
                    while condicao==1: #---luta---
                        ler_texto("intro.txt",46,51)
                        resposta=str(input())
                        condicao=batalha(resposta)
                        if condicao==3:
                            print("fim de jogo\n Acabaram as esperanças!!")
                            start==False
                        elif condicao==2:
                            ler_texto("intro.txt",52,57)
                            pass
                

                elif resposta == 2 :
                    pass
            elif resposta == 2 :
                pass
        elif resposta == 2:
            ler_texto("intro.txt",25,30)
            resposta=int(input())
            if resposta == 1 :
                condicao=1
                while condicao==1: #---luta---
                    ler_texto("intro.txt",46,51)
                    resposta=str(input())
                    condicao=batalha(resposta)
                    if condicao==3:
                        print("fim de jogo\n Acabaram as esperanças!!")
                        start==False
                    elif condicao==2:
                        ler_texto("intro.txt",52,57)
                        pass
                ler_texto("intro.txt",66,72)
                resposta=int(input())
                if resposta==1:
                    pass
                elif resposta==2:
                    ler_texto("intro.txt",73,77)
                    start==False
                    

            elif resposta == 2 :
                ler_texto("intro.txt",58,65)
                start==False
                
        
    
        start=False
    
main()