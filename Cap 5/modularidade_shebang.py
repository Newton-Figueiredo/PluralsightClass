'''
shebang significa esse conjunto de simbolo: " #! " mas na verdade ele é muito importante 
para quando vamos fazer script executaveis, quando escrevemos um arquivo.py 
normalmente executamos o terminal e chamamos o python para só assim chamar o arquivo
que queremos executar.

mas existe a possibilidade de fazer com que o arquivo ja execute o codigo desde que 
indiquemos que versao de python ele deve usar para se executar ...

é ai onde entra o shebang

para fazer um script rodar sem ter que abrir o terminal faça:

#!/usr/bin/env python
ou
#!/usr/bin/env python3

exemplo:
'''
#!/usr/bin/env python
print("ola mundo")

'''
para executar vá no terminal ...
no terminal use :

./nome_do_arquivo.py

caso dé erro de permissao use:

chmod a+x nome_do_arquivo.py
''' 