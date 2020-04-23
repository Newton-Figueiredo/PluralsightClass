from random import randint

ME_ADVINHE = randint(1,100)
CONTADOR = 0
NUMEROS_CHUTADOS=set()

def progress(numeros_chutados):
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

while switch_button == "s" or switch_button == "S":
   
    print(100*"-"+"\n")
    chute=int(input("CHUTE UM NUMERO:\n "))
    
    if chute not in NUMEROS_CHUTADOS:
        
        CONTADOR += 1
        NUMEROS_CHUTADOS.add(chute)

        if chute == ME_ADVINHE:
            if CONTADOR <= 2:
                print(100*"-"+"\n")
                print("PUTA MERDAAA, VAI TOMAR NO SEEU CÚ!! ,BIXO CAGADO DO CARALHOOOOO!!!!\n ")
                switch_button=False
            else:
                print(100*"-"+"\n")
                print("AEWWWW CARRAAAIIII VOCE ACERTOUUUUU KKKKKK\n ")
                switch_button=False
        else:
            if ME_ADVINHE - chute < 0:
                print("EITAAAA VIADOOO DIMINUA MAIS UM POUQUINHO KKKKKK\n ") 
            elif ME_ADVINHE - chute > 0:
                print("CARAI MANO AUMENTE MAIS AI KKKKKK\n ") 
                    
        print(f"\nNUMERO DE TENTATIVAS: {CONTADOR}\n")
        print(f"SEU PROGRESSO:\n {progress(NUMEROS_CHUTADOS)} ")
        print(100*"-"+"\n")

    else:
        print(100*"-"+"\n")
        print("VOCE JÁ CHUTOU ESSE NUMERO KKKKKK\n ")
        
        
       
