from random import randint


def progress(numeros_chutados):
    progresso = []
    for i in range(1,101):
        if i in numeros_chutados:
            progresso.append("x")
        else:
            progresso.append(i)
    return progresso


def main():
    me_advinhe = randint(1,100)
    numeros_chutados=set()
    barra = 100*"-"+"\n"

    print(barra)
    print("SEJAM BEM VINDOS AO CHUTE UM NUMERO!!!\n ")
    print("O OBJETIVO DO JOGO:\nACERTAR UM NUMERO ENTRE 1 - 100 COM O MENOR NUMERO DE TENTATIVAS.\n ")
    print("SIMPLES, NÉ NÃO !?\n")
    switch_button=str(input("VAMOS COMEÇAR: (S)im OU (N)ão \n"))
    print(barra)

    while switch_button in ["s","S"]:
    
        print(barra)
        chute=int(input("CHUTE UM NUMERO:\n "))

        if chute not in numeros_chutados:


            numeros_chutados.add(chute)

            if chute == me_advinhe:
                if len(numeros_chutados) <= 2:
                    print(barra)
                    print("PUTA MERDAAA, VAI TOMAR NO SEEU CÚ!! ,BIXO CAGADO DO CARALHOOOOO!!!!\n ")
                else:
                    print(barra)
                    print("AEWWWW CARRAAAIIII VOCE ACERTOUUUUU KKKKKK\n ")

                switch_button=False

            else:
                if me_advinhe - chute < 0:
                    print("EITAAAA VIADOOO DIMINUA MAIS UM POUQUINHO KKKKKK\n ") 
                elif me_advinhe - chute > 0:
                    print("CARAI MANO AUMENTE MAIS AI KKKKKK\n ") 

            print(f"\nNUMERO DE TENTATIVAS: {len(numeros_chutados)}\n")
            print(f"SEU PROGRESSO:\n {progress(numeros_chutados)} ")
            print(barra)

        else:
            print(barra)
            print("VOCE JÁ CHUTOU ESSE NUMERO KKKKKK\n ")

if __name__ == "__main__" :
        main()
