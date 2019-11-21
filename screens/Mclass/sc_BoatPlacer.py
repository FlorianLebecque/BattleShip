from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from functools import partial

class sc_BoatPlacer(Screen):

    ButtonGrid = []

    def onLoad(self):
        #GridLayout
        GL = self.ids.GL

        #clear all data
        ButtonGrid = []
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
            ButtonGrid.append(ButtonRow)


    def b_onclick(self,*args):
        B = args[0]
        B.text = "O"