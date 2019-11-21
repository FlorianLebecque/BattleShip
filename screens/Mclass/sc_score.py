from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
import json

class sc_score(Screen):
    def getdata(self):

        RV = self.ids.myRv

        myScore = ["j1 : 12","j2 : 56","j2 : 1"]
        Str_Score = []

        with open('data.json') as json_file:
            myScore = json.load(json_file)
            for p in myScore['score']:
                a = ('Name: ' + p['name'])
                b = ('  Score: ' + p['score'])
                
                Str_Score.append(a+b)
       
        print(Str_Score)
        
        RV.data = [{'text': s} for s in Str_Score]

