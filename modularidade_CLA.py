#------------- Argumento das linhas de Comando ---------------
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
    return story_words

def print_words(story_words):
    for word in story_words:
        print(word)

def main():
    words=fetch_words()
    print_words(words)

    
if __name__ == "__main__" :
    main()
'''
# uma outra maneira de importar essas funçoes no terminal do python é usar:
# from modularidade_CLA import *
# o asteristo "*" indica que estamos importanto todas as funçoes e modulos 
#nao é muito indicado fazer isso para nao dar problemas com outras importaçoes 


# outra forma de executarmos o mesmo codigo 
import sys
from urllib.request import urlopen 

def fetch_words(url):
    
    story=urlopen(url)
    story_words=[]

    for line in story:
        line_words=line.decode("utf8").split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words

def print_itens(itens):
    for iten in itens:
        print(iten)


def main(url):
    words=fetch_words(url)
    print_itens(words)

    
if __name__ == "__main__" :
    main(sys.argv[1])