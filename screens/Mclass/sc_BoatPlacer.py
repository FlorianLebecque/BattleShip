from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from functools import partial

class sc_BoatPlacer(Screen):

    ButtonGrid = []

    def onLoad(self):
        #GridLayout
        GL = self.ids.GL

        #clear all data
        
        self.ButtonGrid = []
        GL.children.clear()

        #generation of the buttons grid
        for i in range(0,10):
            ButtonRow = []
            for j in range(0,10):
                b = Button()
                b.name = str(i)+":"+str(j)
                b.font_size="20sp"
                b.bind(on_release=self.b_onclick)
               # b.on_release= self.b_onclick()
                ButtonRow.append(b)
                GL.add_widget(b)
            self.ButtonGrid.append(ButtonRow)


    def b_onclick(self,*args):
        B = args[0]
        B.text = "O"

    def convertion(self,Fichier):
        file= open(Fichier, 'r')
        a=[]
        for line in file:
            a.append(line)

        for i in range(len(a)):
            a[i]=a[i].strip()
        print(a)

        file.close()            #convertir le fichier txt en python, on obtient tout le tableau avec les * et les lettres

        map=[]

        for i in range(1,11):
            grenier=[]
            for j in range (1,11):
                if a[i][j] in 'tscp':
                    grenier.append(1)
                    self.ButtonGrid[i-1][j-1].text = "O"
                else:
                    grenier.append(0)       
            map.append(grenier)
        print(map)
        return map
