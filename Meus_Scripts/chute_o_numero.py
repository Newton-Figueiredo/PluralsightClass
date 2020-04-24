from random import randint

def barra():
    return print(100*"-"+"\n")
def progress(numeros_chutados):
    progresso = []
    for i in range(1,101):
        if i in numeros_chutados:
            progresso.append("x")
        else:
            progresso.append(i)
    return progresso
def main():
    ME_ADVINHE = randint(1,100)
    NUMEROS_CHUTADOS=set()

    barra()
    print("SEJAM BEM VINDOS AO CHUTE UM NUMERO!!!\n ")
    print("O OBJETIVO DO JOGO:\nACERTAR UM NUMERO ENTRE 1 - 100 COM O MENOR NUMERO DE TENTATIVAS.\n ")
    print("SIMPLES, NÉ NÃO !?\n")
    switch_button=str(input("VAMOS COMEÇAR: (S)im OU (N)ão \n"))
    barra()

    while switch_button in ["s","S"]:
    
        barra()
        chute=int(input("CHUTE UM NUMERO:\n "))

        if chute not in NUMEROS_CHUTADOS:


            NUMEROS_CHUTADOS.add(chute)

            if chute == ME_ADVINHE:
                if len(NUMEROS_CHUTADOS) <= 2:
                    barra()
                    print("PUTA MERDAAA, VAI TOMAR NO SEEU CÚ!! ,BIXO CAGADO DO CARALHOOOOO!!!!\n ")
                else:
                    barra()
                    print("AEWWWW CARRAAAIIII VOCE ACERTOUUUUU KKKKKK\n ")

                switch_button=False

            else:
                if ME_ADVINHE - chute < 0:
                    print("EITAAAA VIADOOO DIMINUA MAIS UM POUQUINHO KKKKKK\n ") 
                elif ME_ADVINHE - chute > 0:
                    print("CARAI MANO AUMENTE MAIS AI KKKKKK\n ") 

            print(f"\nNUMERO DE TENTATIVAS: {len(NUMEROS_CHUTADOS)}\n")
            print(f"SEU PROGRESSO:\n {progress(NUMEROS_CHUTADOS)} ")
            barra()

        else:
            barra()
            print("VOCE JÁ CHUTOU ESSE NUMERO KKKKKK\n ")

main()
