def ler_texto(nome_do_arquivo,linha_inicio,linha_fim):
    f=open(nome_do_arquivo,mode='rt',encoding='utf-8')
    lines=f.readlines()
    contador=1
    for line in lines:
        if contador<=linha_fim and contador>=linha_inicio:
            print(line)
        contador+=1
    f.close()

def main(start):
    while start==True:
        

print("""

  ____    _    _  _  _    _                      _____                          _  _                      
 / __ \  | |  | || || |  (_)                    / ____|                        | || |                     
| |  | | | |  | || || |_  _  _ __ ___    ___   | |      ___   _ __   ___   ___ | || |__    ___            
| |  | | | |  | || || __|| || '_ ` _ \  / _ \  | |     / _ \ | '_ \ / __| / _ \| || '_ \  / _ \           
| |__| | | |__| || || |_ | || | | | | || (_) | | |____| (_) || | | |\__ \|  __/| || | | || (_) |  _  _  _ 
 \____/   \____/ |_| \__||_||_| |_| |_| \___/   \_____|\___/ |_| |_||___/ \___||_||_| |_| \___/  (_)(_)(_)
""")

start=str(input("Aperte qualquer tecla para começar."))

