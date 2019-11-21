import glob

#kivy stuff
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder

#kivy uix for gui interface
from kivy.graphics import Color, Rectangle  #allow me to have a background for the layout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import ScreenManager, Screen

#import all screens
from screens.Mclass.sc_menu import sc_menu
from screens.Mclass.sc_BoatPlacer import sc_BoatPlacer
from screens.Mclass.sc_score import sc_score

#loading all screens gui
Builder.load_file("screens/globalRules.kv")
gui_files = glob.glob("screens/gui/*.kv")
for gui_file in gui_files :
    Builder.load_file(gui_file)

#adding the screens to the screens manager
sm = ScreenManager()
sm.add_widget(sc_menu(name="sc_menu"))
sm.add_widget(sc_BoatPlacer(name="sc_BoatPlacer"))
sm.add_widget(sc_score(name="sc_score"))
#sm.current = "sc_BoatPlacer"

#global variable
GAME_TYPE = 0; #Player against player , 1 = player against computer

#main class
class BattleShip(App):

    def build(self):
        return sm


if __name__ == '__main__':
    BattleShip().run()