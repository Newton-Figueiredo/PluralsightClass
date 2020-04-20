#para começar essa aula devemos adaptar um codigo de uma aula passada em uma função 
#esse codigo pega um texto na internet e o transforma em palavras.
'''
def fetch_words():
    from urllib.request import urlopen
    story=urlopen("http://sixty-north.com/c/t.txt")
    story_words=[]

    for line in story:
        line_words=line.decode("utf8").split()
        for word in line_words:
            story_words.append(word)

    story.close()

    for word in story_words:
        print(word)

    if __name__ == "__main__" :
        print('me executou pelo terminal')
    else:
        print('me executou como um módulo')
'''
#a aula ta ensinando a como chamar essa função no terminal 
#ele ensina 2 maneiras nas quais vou mostrar agora:
#no terminal chame pyhton3:
'''
import modularidade_name 
modularidade_name.fetch_words()
# ou
from modularidade_name import fetch_words
fetch_words()

'''
'''o video mostra que se abrirmos o arquivo python pelo terminal
 ele nao chama a função. 
apenas abre o arquivo.. existe uma maneira de quando abrirmos o arquivo
 ele já execute uma função
 sem precisar chama-la: usaremos __name__ 
 
 if __name__ == '__main__':
    print('me executou pelo terminal')
else:
    print('me executou como um módulo')
 
 para que a função já seja executada quando chamarmos o arquivo pelo terminal
 devemos fazer dessa maneira: (fora da função) , mas no mesmo arquivo.
 
 if __name__ == '__main__':
    nome_da_funcao()

'''

def fetch_words():
    from urllib.request import urlopen
    story=urlopen("http://sixty-north.com/c/t.txt")
    story_words=[]

    for line in story:
        line_words=line.decode("utf8").split()
        for word in line_words:
            story_words.append(word)

    story.close()

    for word in story_words:
        print(word)

if __name__ == "__main__" :
        fetch_words()
 

