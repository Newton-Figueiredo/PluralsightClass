from random import randint

def Progresso(numeros_chutados):
    progresso = []
    for i in range(1,101):
        if i in numeros_chutados:
            progresso.append("x")
        else:
            progresso.append(i)
    return progresso


print(100*"-"+"\n")
print("SEJAM BEM VINDOS AO CHUTE UM NUMERO!!!\n ")
print("O OBJETIVO DO JOGO:\nACERTAR UM NUMERO ENTRE 1 - 100 COM O MENOR NUMERO DE TENTATIVAS.\n ")
print("SIMPLES, NÉ NÃO !?\n")
switch_button=str(input("VAMOS COMEÇAR: (S)im OU (N)ão \n"))
print("\n"+100*"-"+"\n")


#------variaveis globais -------
me_advinhe = randint(1,100)
contador = 0
numeros_chutados=set()

#------------------------------
#print(me_advinhe)
while switch_button == "s" or switch_button == "S":
   
    print(100*"-"+"\n")
    chute=int(input("CHUTE UM NUMERO:\n "))
    
    if chute not in numeros_chutados:
        
        contador += 1
        numeros_chutados.add(chute)

        if chute == me_advinhe:
            if contador <= 2:
                print(100*"-"+"\n")
                print("PUTA MERDAAA, VAI TOMAR NO SEEU CÚ!! ,BIXO CAGADO DO CARALHOOOOO!!!!\n ")
                switch_button=False
            else:
                print(100*"-"+"\n")
                print("AEWWWW CARRAAAIIII VOCE ACERTOUUUUU KKKKKK\n ")
                switch_button=False
        elif chute > me_advinhe - 10 and chute < me_advinhe + 10 :
            
            print("CARALHOOOO TA QUASE LÁ KKKKKK \n")    
        elif chute > me_advinhe - 25 and chute < me_advinhe + 25 :
            
            print("EITAAAA VIADOOO QUE TA PERTINHO KKKKKK\n ")
            
        elif chute > me_advinhe + 25 and chute < me_advinhe - 25:
            
            print("VISH PASSOU FOI LONGE KKKKKK \n")
        
        
        print(f"\nNUMERO DE TENTATIVAS: {contador}\n")
        print(f"SEU PROGRESSO:\n {Progresso(numeros_chutados)} ")
        print(100*"-"+"\n")

    else:
        print(100*"-"+"\n")
        print("VOCE JÁ CHUTOU ESSE NUMERO KKKKKK\n ")
        
        
       
