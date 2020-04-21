import PySimpleGUI as sg

from random import choice 

class TelaDG:
    def __init__(self):
        #layout (define estilos)
        layout=[
            [sg.Text("Partiu rogar esse RPG!!!!!!")],
            [sg.Text("quantos dados")],
            [sg.Slider(range=(1,30),default_value=0,orientation="h",size=(10,10),key="ndados")],
            [sg.Text("quantos lados")],
            [sg.Slider(range=(1,30),default_value=0,orientation="h",size=(10,10),key="nlados")],
            [sg.Button("GO")],
            [sg.Output(size=(30,20))]
        ]
        #janela
        self.janela = sg.Window("Dice Gerator").layout(layout)
        
        

    def Iniciar(self):
        Dados=[]
        Lados=[]
        while True:
            #extrair os dados da tela
            self.button, self.values = self.janela.Read()
            ndados = int(self.values["ndados"])
            nlados = int(self.values["nlados"])

            for lados in range(nlados):
                Lados.append(lados+1)

            nndados=ndados

            if ndados >=2 and nlados >0 :
                print("Lançando os Dados!!!!")
                for dados in range(nndados):
                    Dados.append(Lados)
                    print(f"Valor do Dado Nº:{dados+1} é: {choice(Dados[dados])}")
            elif ndados == 1 and nlados >0 :
                print("Lançando o Dados!!!!")
                print(f"Valor do Dado é: {choice(Lados)}")
            
            

tela = TelaDG()
tela.Iniciar()